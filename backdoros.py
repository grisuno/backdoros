#!/usr/bin/env python3

import sys
import socket
import imp
import asyncore
import io  # Cambiado a io en Python 3
import platform
import urllib.request  # Cambiado a urllib.request en Python 3
import asynchat
import warnings
import datetime
import subprocess
import getpass
import os
import shlex
import multiprocessing
import code

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
# Clases #
###########

class IOProxy(object):
    def __init__(self, proxy, prefix=''):
        self._proxy = proxy
        self._prefix = prefix

    def write(self, str):
        # Special Char?
        if str == '\n' or str == '\t' or str == '\r':
            self._proxy.push(str)
        else:
            self._proxy.push('%s: %s' % (self._prefix, str))


class VirtualFile(io.StringIO):  # Cambiado a io.StringIO
    def __init__(self, *args, **kwargs):
        super(VirtualFile, self).__init__(*args, **kwargs)
        self.__total_size = 0

    def read(self, *args, **kwargs):
        _size = None
        try:
            _size = kwargs.get('size', args[0])
        except IndexError:
            pass

        return self.getvalue()[:_size]

    def write(self, str):
        global _mem_storage_size
        super(VirtualFile, self).write(str)
        self.__total_size += len(str)
        _mem_storage_size += self.__total_size

    def close(self, force=False):
        global _mem_storage_size
        if force:
            _mem_storage_size -= self.__total_size
            super(VirtualFile, self).close()

    def getsize(self):
        return self.__total_size

    def __exit__(self, type, value, traceback):
        return None

    def __enter__(self):
        return self


class ShellHandler(asynchat.async_chat):
    def __init__(self, *args, **kwargs):
        super(ShellHandler, self).__init__(*args, **kwargs)
        self._childs = {}
        self._in_repl = False
        self._repl_instance = code.InteractiveConsole()
        self._stdout = None
        self._stderr = None
        self._in_cat = False
        self._in_cat_buffer = ""
        self._in_cat_filename = ""
        self.buffer = ""
        self.set_terminator(b'\n')  # Se cambia el terminador a bytes para compatibilidad

        # Bienvenida
        self.push(f"BackdorOS release {__version__} on an {platform.platform()}\n")
        self.push("%> ")

    def collect_incoming_data(self, data):
        self.buffer += data.decode("utf-8")  # Decodificación de bytes a string

    def found_terminator(self):
        if self.buffer:
            self.parse(self.buffer + '\n')
        self.buffer = ""

    #########################
    # BackdorOS Basic Shell #
    #########################

    _COMMANDS = {
        "WRITE": {"DESC": "write file to mem", "USAGE": "[-|url] [filename]", "ARGC": 2},
        "READ": {"DESC": "read file from mem/disk", "USAGE": "[path]", "ARGC": 1},
        "DELETE": {"DESC": "delete file from mem", "USAGE": "[filename]", "ARGC": 1},
        "DIR": {"DESC": "list all files on mem"},
        "PYGO": {"DESC": "start python program from mem/disk", "USAGE": "[progname|progname.funcname] [args ...]", "ARGC": 1},
        "PPYGO": {"DESC": "like PYGO but run as a separate process", "USAGE": "[progname|progname.funcname] [args ...]", "ARGC": 1},
        "PYEXECFILE": {"DESC": "exec python program from mem/disk", "USAGE": "[filename]", "ARGC": 1},
        "HELP": {"DESC": "print this screen"},
        "REBOOT": {"DESC": "stopping and restarting the system"},
        "SHUTDOWN": {"DESC": "close down the system"},
        "QUIT": {"DESC": "close this session"},
        "UPTIME": {"DESC": "print how long the system has been running"},
        "SHEXEC": {"DESC": "execute system command and print the output", "USAGE": "[command]", "ARGC": 1},
        "PSHEXEC": {"DESC": "like SHEXEC but run as a separate process", "USAGE": "[command]", "ARGC": 1},
        "PJOINALL": {"DESC": "join all child processes with timeout of 1 sec"},
        "PLIST": {"DESC": "list all child processes"},
        "DEBUG": {"DESC": "toggle debug mode", "USAGE": "[true|false|status]", "ARGC": 1},
        "PYREPL": {"DESC": "python in-memory REPL"},
        "CLS": {"DESC": "attempt to clear the screen"}
    }

    # Cambiar todos los métodos según sea necesario para print, manejo de bytes, etc.

