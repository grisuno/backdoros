# root

*Community 0 | 3 files | cohesion 1.00*

## Definition

This community groups 3 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `IOProxy`, `Memory`, `ShellHandler`, `ShellServer`, `VirtualFile`, `__init__`, `_do_DELETE`, `_do_DIR`. Core file: `backdoros.py` (29 symbols). Documented purpose: Copyright (c) 2019, SafeBreach All rights reserved.  Redistribution and use in source and binary forms, with or without modification, are permitted provided tha.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `backdoros.py` | py | utility | 29 | no |
| `fuse_inmem_fs.py` | py | utility | 24 | yes |
| `getbanners.py` | py | utility | 2 | yes |

## Key Symbols

- `IOProxy` (class, `backdoros.py:37`) `class IOProxy`
- `__init__` (method, `backdoros.py:38`) `def __init__(self, proxy, prefix)`
- `write` (method, `backdoros.py:42`) `def write(self, str)`
- `VirtualFile` (class, `backdoros.py:49`) `class VirtualFile(StringIO)`
- `__init__` (method, `backdoros.py:50`) `def __init__(self)`
- `write` (method, `backdoros.py:54`) `def write(self, str)`
- `close` (method, `backdoros.py:60`) `def close(self, force)`
- `getsize` (method, `backdoros.py:66`) `def getsize(self)`
- `ShellHandler` (class, `backdoros.py:69`) `class ShellHandler(Protocol)`
- `__init__` (method, `backdoros.py:70`) `def __init__(self, loop)`
- `connection_made` (method, `backdoros.py:83`) `def connection_made(self, transport)`
- `data_received` (method, `backdoros.py:87`) `def data_received(self, data)`
- `process_buffer` (method, `backdoros.py:91`) `def process_buffer(self)`
- `parse` (method, `backdoros.py:96`) `def parse(self, data)`
- `_unknown_command` (method, `backdoros.py:142`) `def _unknown_command(self, params)`
- `_do_WRITE` (method, `backdoros.py:145`) `def _do_WRITE(self, params)`
- `_do_READ` (method, `backdoros.py:157`) `def _do_READ(self, params)`
- `_do_DELETE` (method, `backdoros.py:163`) `def _do_DELETE(self, params)`
- `_do_DIR` (method, `backdoros.py:170`) `def _do_DIR(self, params)`
- `_do_HELP` (method, `backdoros.py:175`) `def _do_HELP(self, params)`
- `_do_QUIT` (method, `backdoros.py:181`) `def _do_QUIT(self, params)`
- `_do_REBOOT` (method, `backdoros.py:185`) `def _do_REBOOT(self, params)`
- `_do_SHUTDOWN` (method, `backdoros.py:188`) `def _do_SHUTDOWN(self, params)`
- `_do_UPTIME` (method, `backdoros.py:193`) `def _do_UPTIME(self, params)`
- `ShellServer` (class, `backdoros.py:197`) `class ShellServer`
- `__init__` (method, `backdoros.py:198`) `def __init__(self, host, port)`
- `start_server` (method, `backdoros.py:202`) `def start_server(self)`
- `create_shell_handler` (method, `backdoros.py:207`) `def create_shell_handler(self, reader, writer)`
- `main` (method, `backdoros.py:216`) `def main()`
- `Memory` (class, `fuse_inmem_fs.py:61`) `class Memory(Operations)` - Example memory filesystem. Supports only one level of files.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- [taint medium] `backdoros.py` -> `backdoros.py` via `urllib.request` (0 hops)
- [taint high] `backdoros.py` -> `backdoros.py` via `subprocess` (0 hops)
- [dataflow UNCHECKED_ALLOC] `backdoros.py:152` `_do_WRITE` `output_data`: Result of allocator stored in `output_data` is never checked against NULL.
- [dataflow UNCHECKED_ALLOC] `getbanners.py:69` `main` `s`: Result of allocator stored in `s` is never checked against NULL.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `backdoros.py`)? What purpose do they serve?
- Is the dangerous import `urllib.request` in `backdoros.py` still required, or can it be isolated?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `backdoros.py`
- `fuse_inmem_fs.py`
- `getbanners.py`
