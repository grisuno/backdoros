# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 3 | **Total Symbols Extracted:** 55 | **Total Imports:** 25

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    backdoros_py["backdoros.py (py)"]
    class backdoros_py mod;
    backdoros_py_IOProxy["IOProxy"]
    class backdoros_py_IOProxy cls;
    backdoros_py --> backdoros_py_IOProxy
    backdoros_py_VirtualFile["VirtualFile"]
    class backdoros_py_VirtualFile cls;
    backdoros_py --> backdoros_py_VirtualFile
    backdoros_py_ShellHandler["ShellHandler"]
    class backdoros_py_ShellHandler cls;
    backdoros_py --> backdoros_py_ShellHandler
    backdoros_py_ShellServer["ShellServer"]
    class backdoros_py_ShellServer cls;
    backdoros_py --> backdoros_py_ShellServer
    backdoros_py_main["main"]
    class backdoros_py_main fn;
    backdoros_py --> backdoros_py_main
    fuse_inmem_fs_py["fuse_inmem_fs.py (py)"]
    class fuse_inmem_fs_py mod;
    fuse_inmem_fs_py_Memory["Memory"]
    class fuse_inmem_fs_py_Memory cls;
    fuse_inmem_fs_py --> fuse_inmem_fs_py_Memory
    fuse_inmem_fs_py_main["main"]
    class fuse_inmem_fs_py_main fn;
    fuse_inmem_fs_py --> fuse_inmem_fs_py_main
    fuse_inmem_fs_py___init__["__init__"]
    class fuse_inmem_fs_py___init__ fn;
    fuse_inmem_fs_py --> fuse_inmem_fs_py___init__
    fuse_inmem_fs_py_chmod["chmod"]
    class fuse_inmem_fs_py_chmod fn;
    fuse_inmem_fs_py --> fuse_inmem_fs_py_chmod
    fuse_inmem_fs_py_chown["chown"]
    class fuse_inmem_fs_py_chown fn;
    fuse_inmem_fs_py --> fuse_inmem_fs_py_chown
    getbanners_py["getbanners.py (py)"]
    class getbanners_py mod;
    getbanners_py_slugify["slugify"]
    class getbanners_py_slugify fn;
    getbanners_py --> getbanners_py_slugify
    getbanners_py_main["main"]
    class getbanners_py_main fn;
    getbanners_py --> getbanners_py_main
    ext_sys["sys"]
    class ext_sys ext;
    backdoros_py -.->|imports| ext_sys
    ext_socket["socket"]
    class ext_socket ext;
    backdoros_py -.->|imports| ext_socket
    ext_importlib_util["importlib.util"]
    class ext_importlib_util ext;
    backdoros_py -.->|imports| ext_importlib_util
    ext_asyncio["asyncio"]
    class ext_asyncio ext;
    backdoros_py -.->|imports| ext_asyncio
    ext_io["io"]
    class ext_io ext;
    backdoros_py -.->|imports| ext_io
    ext_platform["platform"]
    class ext_platform ext;
    backdoros_py -.->|imports| ext_platform
    ext_urllib_request["urllib.request"]
    class ext_urllib_request ext;
    backdoros_py -.->|imports| ext_urllib_request
    ext_datetime["datetime"]
    class ext_datetime ext;
    backdoros_py -.->|imports| ext_datetime
    ext_subprocess["subprocess"]
    class ext_subprocess ext;
    backdoros_py -.->|imports| ext_subprocess
    ext_getpass["getpass"]
    class ext_getpass ext;
    backdoros_py -.->|imports| ext_getpass
    ext_os["os"]
    class ext_os ext;
    backdoros_py -.->|imports| ext_os
    ext_shlex["shlex"]
    class ext_shlex ext;
    backdoros_py -.->|imports| ext_shlex
    ext_multiprocessing["multiprocessing"]
    class ext_multiprocessing ext;
    backdoros_py -.->|imports| ext_multiprocessing
    ext_code["code"]
    class ext_code ext;
    backdoros_py -.->|imports| ext_code
    ext_warnings["warnings"]
    class ext_warnings ext;
    backdoros_py -.->|imports| ext_warnings
    fuse_inmem_fs_py -.->|imports| ext_sys
    ext_logging["logging"]
    class ext_logging ext;
    fuse_inmem_fs_py -.->|imports| ext_logging
    ext_collections["collections"]
    class ext_collections ext;
    fuse_inmem_fs_py -.->|imports| ext_collections
    ext_errno["errno"]
    class ext_errno ext;
    fuse_inmem_fs_py -.->|imports| ext_errno
    ext_stat["stat"]
    class ext_stat ext;
    fuse_inmem_fs_py -.->|imports| ext_stat
    ext_time["time"]
    class ext_time ext;
    fuse_inmem_fs_py -.->|imports| ext_time
    ext_fuse["fuse"]
    class ext_fuse ext;
    fuse_inmem_fs_py -.->|imports| ext_fuse
    getbanners_py -.->|imports| ext_socket
    getbanners_py -.->|imports| ext_sys
    getbanners_py -.->|imports| ext_os
```

---

## Architecture Reference

### PY (3 files)

#### `backdoros.py`
**Path:** `backdoros.py`

**Classes:**
- `IOProxy` (line 37) `class IOProxy`
- `VirtualFile` (line 49) `class VirtualFile`
- `ShellHandler` (line 69) `class ShellHandler`
- `ShellServer` (line 197) `class ShellServer`

**Functions:**
- `main` (line 216) `def main()`
- `__init__` (line 38) `def __init__(self, proxy, prefix)`
- `write` (line 42) `def write(self, str)`
- `__init__` (line 50) `def __init__(self)`
- `write` (line 54) `def write(self, str)`
- `close` (line 60) `def close(self, force)`
- `getsize` (line 66) `def getsize(self)`
- `__init__` (line 70) `def __init__(self, loop)`
- `connection_made` (line 83) `def connection_made(self, transport)`
- `data_received` (line 87) `def data_received(self, data)`
- `process_buffer` (line 91) `def process_buffer(self)`
- `parse` (line 96) `def parse(self, data)`
- `_unknown_command` (line 142) `def _unknown_command(self, params)`
- `_do_WRITE` (line 145) `def _do_WRITE(self, params)`
- `_do_READ` (line 157) `def _do_READ(self, params)`
- `_do_DELETE` (line 163) `def _do_DELETE(self, params)`
- `_do_DIR` (line 170) `def _do_DIR(self, params)`
- `_do_HELP` (line 175) `def _do_HELP(self, params)`
- `_do_QUIT` (line 181) `def _do_QUIT(self, params)`
- `_do_REBOOT` (line 185) `def _do_REBOOT(self, params)`
- `_do_SHUTDOWN` (line 188) `def _do_SHUTDOWN(self, params)`
- `_do_UPTIME` (line 193) `def _do_UPTIME(self, params)`
- `__init__` (line 198) `def __init__(self, host, port)`
- `start_server` (line 202) `def start_server(self)`
- `create_shell_handler` (line 207) `def create_shell_handler(self, reader, writer)`

#### `fuse_inmem_fs.py`
**Path:** `fuse_inmem_fs.py`

**Classes:**
- `Memory` (line 61) `class Memory(Operations)` - *Example memory filesystem. Supports only one level of files.*

**Functions:**
- `main` (line 199) `def main(argc, argv)`
- `__init__` (line 64) `def __init__(self)`
- `chmod` (line 76) `def chmod(self, path, mode)`
- `chown` (line 81) `def chown(self, path, uid, gid)`
- `create` (line 85) `def create(self, path, mode)`
- `getattr` (line 97) `def getattr(self, path, fh)`
- `getxattr` (line 103) `def getxattr(self, path, name, position)`
- `listxattr` (line 111) `def listxattr(self, path)`
- `mkdir` (line 115) `def mkdir(self, path, mode)`
- `open` (line 126) `def open(self, path, flags)`
- `read` (line 130) `def read(self, path, size, offset, fh)`
- `readdir` (line 133) `def readdir(self, path, fh)`
- `readlink` (line 136) `def readlink(self, path)`
- `removexattr` (line 139) `def removexattr(self, path, name)`
- `rename` (line 147) `def rename(self, old, new)`
- `rmdir` (line 151) `def rmdir(self, path)`
- `setxattr` (line 156) `def setxattr(self, path, name, value, options, position)`
- `statfs` (line 161) `def statfs(self, path)`
- `symlink` (line 164) `def symlink(self, target, source)`
- `truncate` (line 172) `def truncate(self, path, length, fh)`
- `unlink` (line 178) `def unlink(self, path)`
- `utimens` (line 182) `def utimens(self, path, times)`
- `write` (line 188) `def write(self, path, data, offset, fh)`

#### `getbanners.py`
**Path:** `getbanners.py`

**Functions:**
- `slugify` (line 54) `def slugify(input)`
- `main` (line 58) `def main(argc, argv)`
