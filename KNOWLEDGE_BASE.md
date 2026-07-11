# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis.

**Total Files Parsed:** 3 | **Total Symbols Extracted:** 55 | **Total Imports:** 25

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa;
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

**Classs:**
- `IOProxy` (line 37)
- `VirtualFile` (line 49)
- `ShellHandler` (line 69)
- `ShellServer` (line 197)

**Functions:**
- `main` (line 216)
- `__init__` (line 38)
- `write` (line 42)
- `__init__` (line 50)
- `write` (line 54)
- `close` (line 60)
- `getsize` (line 66)
- `__init__` (line 70)
- `connection_made` (line 83)
- `data_received` (line 87)
- `process_buffer` (line 91)
- `parse` (line 96)
- `_unknown_command` (line 142)
- `_do_WRITE` (line 145)
- `_do_READ` (line 157)
- `_do_DELETE` (line 163)
- `_do_DIR` (line 170)
- `_do_HELP` (line 175)
- `_do_QUIT` (line 181)
- `_do_REBOOT` (line 185)
- `_do_SHUTDOWN` (line 188)
- `_do_UPTIME` (line 193)
- `__init__` (line 198)
- `start_server` (line 202)
- `create_shell_handler` (line 207)

#### `fuse_inmem_fs.py`
**Path:** `fuse_inmem_fs.py`

**Classs:**
- `Memory` (line 61) - *Example memory filesystem. Supports only one level of files.*

**Functions:**
- `main` (line 199)
- `__init__` (line 64)
- `chmod` (line 76)
- `chown` (line 81)
- `create` (line 85)
- `getattr` (line 97)
- `getxattr` (line 103)
- `listxattr` (line 111)
- `mkdir` (line 115)
- `open` (line 126)
- `read` (line 130)
- `readdir` (line 133)
- `readlink` (line 136)
- `removexattr` (line 139)
- `rename` (line 147)
- `rmdir` (line 151)
- `setxattr` (line 156)
- `statfs` (line 161)
- `symlink` (line 164)
- `truncate` (line 172)
- `unlink` (line 178)
- `utimens` (line 182)
- `write` (line 188)

#### `getbanners.py`
**Path:** `getbanners.py`

**Functions:**
- `slugify` (line 54)
- `main` (line 58)
