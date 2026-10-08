# API

## backdoros.py
- `IOProxy.__init__` (method) `backdoros.py:38` `def __init__(self, proxy, prefix)`
- `IOProxy.write` (method) `backdoros.py:42` `def write(self, str)`
- `VirtualFile.__init__` (method) `backdoros.py:50` `def __init__(self)`
- `VirtualFile.write` (method) `backdoros.py:54` `def write(self, str)`
- `VirtualFile.close` (method) `backdoros.py:60` `def close(self, force)`
- `VirtualFile.getsize` (method) `backdoros.py:66` `def getsize(self)`
- `ShellHandler.__init__` (method) `backdoros.py:70` `def __init__(self, loop)`
- `ShellHandler.connection_made` (method) `backdoros.py:83` `def connection_made(self, transport)`
- `ShellHandler.data_received` (method) `backdoros.py:87` `def data_received(self, data)`
- `ShellHandler.process_buffer` (method) `backdoros.py:91` `def process_buffer(self)`
- `ShellHandler.parse` (method) `backdoros.py:96` `def parse(self, data)`
- `ShellServer.__init__` (method) `backdoros.py:198` `def __init__(self, host, port)`
- `ShellServer.start_server` (method) `backdoros.py:202` `def start_server(self)`
- `ShellServer.create_shell_handler` (method) `backdoros.py:207` `def create_shell_handler(self, reader, writer)`
- `ShellServer.main` (method) `backdoros.py:216` `def main()`

## fuse_inmem_fs.py
- `Memory.__init__` (method) `fuse_inmem_fs.py:64` `def __init__(self)`
- `Memory.chmod` (method) `fuse_inmem_fs.py:76` `def chmod(self, path, mode)`
- `Memory.chown` (method) `fuse_inmem_fs.py:81` `def chown(self, path, uid, gid)`
- `Memory.create` (method) `fuse_inmem_fs.py:85` `def create(self, path, mode)`
- `Memory.getattr` (method) `fuse_inmem_fs.py:97` `def getattr(self, path, fh)`
- `Memory.getxattr` (method) `fuse_inmem_fs.py:103` `def getxattr(self, path, name, position)`
- `Memory.listxattr` (method) `fuse_inmem_fs.py:111` `def listxattr(self, path)`
- `Memory.mkdir` (method) `fuse_inmem_fs.py:115` `def mkdir(self, path, mode)`
- `Memory.open` (method) `fuse_inmem_fs.py:126` `def open(self, path, flags)`
- `Memory.read` (method) `fuse_inmem_fs.py:130` `def read(self, path, size, offset, fh)`
- `Memory.readdir` (method) `fuse_inmem_fs.py:133` `def readdir(self, path, fh)`
- `Memory.readlink` (method) `fuse_inmem_fs.py:136` `def readlink(self, path)`
- `Memory.removexattr` (method) `fuse_inmem_fs.py:139` `def removexattr(self, path, name)`
- `Memory.rename` (method) `fuse_inmem_fs.py:147` `def rename(self, old, new)`
- `Memory.rmdir` (method) `fuse_inmem_fs.py:151` `def rmdir(self, path)`
- `Memory.setxattr` (method) `fuse_inmem_fs.py:156` `def setxattr(self, path, name, value, options, position)`
- `Memory.statfs` (method) `fuse_inmem_fs.py:161` `def statfs(self, path)`
- `Memory.symlink` (method) `fuse_inmem_fs.py:164` `def symlink(self, target, source)`
- `Memory.truncate` (method) `fuse_inmem_fs.py:172` `def truncate(self, path, length, fh)`
- `Memory.unlink` (method) `fuse_inmem_fs.py:178` `def unlink(self, path)`
- `Memory.utimens` (method) `fuse_inmem_fs.py:182` `def utimens(self, path, times)`
- `Memory.write` (method) `fuse_inmem_fs.py:188` `def write(self, path, data, offset, fh)`
- `Memory.main` (method) `fuse_inmem_fs.py:199` `def main(argc, argv)`

## getbanners.py
- `slugify` (function) `getbanners.py:54` `def slugify(input)`
- `main` (function) `getbanners.py:58` `def main(argc, argv)`
