# API

## backdoros.py

### main `def main()`
- Defined: `backdoros.py:216`

### __init__ `def __init__(self, proxy, prefix)`
- Defined: `backdoros.py:38`

### write `def write(self, str)`
- Defined: `backdoros.py:42`

### __init__ `def __init__(self)`
- Defined: `backdoros.py:50`

### write `def write(self, str)`
- Defined: `backdoros.py:54`

### close `def close(self, force)`
- Defined: `backdoros.py:60`

### getsize `def getsize(self)`
- Defined: `backdoros.py:66`

### __init__ `def __init__(self, loop)`
- Defined: `backdoros.py:70`

### connection_made `def connection_made(self, transport)`
- Defined: `backdoros.py:83`

### data_received `def data_received(self, data)`
- Defined: `backdoros.py:87`

### process_buffer `def process_buffer(self)`
- Defined: `backdoros.py:91`

### parse `def parse(self, data)`
- Defined: `backdoros.py:96`

### _unknown_command `def _unknown_command(self, params)`
- Defined: `backdoros.py:142`

### _do_WRITE `def _do_WRITE(self, params)`
- Defined: `backdoros.py:145`

### _do_READ `def _do_READ(self, params)`
- Defined: `backdoros.py:157`

### _do_DELETE `def _do_DELETE(self, params)`
- Defined: `backdoros.py:163`

### _do_DIR `def _do_DIR(self, params)`
- Defined: `backdoros.py:170`

### _do_HELP `def _do_HELP(self, params)`
- Defined: `backdoros.py:175`

### _do_QUIT `def _do_QUIT(self, params)`
- Defined: `backdoros.py:181`

### _do_REBOOT `def _do_REBOOT(self, params)`
- Defined: `backdoros.py:185`

### _do_SHUTDOWN `def _do_SHUTDOWN(self, params)`
- Defined: `backdoros.py:188`

### _do_UPTIME `def _do_UPTIME(self, params)`
- Defined: `backdoros.py:193`

### __init__ `def __init__(self, host, port)`
- Defined: `backdoros.py:198`

### start_server `def start_server(self)`
- Defined: `backdoros.py:202`

### create_shell_handler `def create_shell_handler(self, reader, writer)`
- Defined: `backdoros.py:207`

## fuse_inmem_fs.py

### main `def main(argc, argv)`
- Defined: `fuse_inmem_fs.py:199`

### __init__ `def __init__(self)`
- Defined: `fuse_inmem_fs.py:64`

### chmod `def chmod(self, path, mode)`
- Defined: `fuse_inmem_fs.py:76`

### chown `def chown(self, path, uid, gid)`
- Defined: `fuse_inmem_fs.py:81`

### create `def create(self, path, mode)`
- Defined: `fuse_inmem_fs.py:85`

### getattr `def getattr(self, path, fh)`
- Defined: `fuse_inmem_fs.py:97`

### getxattr `def getxattr(self, path, name, position)`
- Defined: `fuse_inmem_fs.py:103`

### listxattr `def listxattr(self, path)`
- Defined: `fuse_inmem_fs.py:111`

### mkdir `def mkdir(self, path, mode)`
- Defined: `fuse_inmem_fs.py:115`

### open `def open(self, path, flags)`
- Defined: `fuse_inmem_fs.py:126`

### read `def read(self, path, size, offset, fh)`
- Defined: `fuse_inmem_fs.py:130`

### readdir `def readdir(self, path, fh)`
- Defined: `fuse_inmem_fs.py:133`

### readlink `def readlink(self, path)`
- Defined: `fuse_inmem_fs.py:136`

### removexattr `def removexattr(self, path, name)`
- Defined: `fuse_inmem_fs.py:139`

### rename `def rename(self, old, new)`
- Defined: `fuse_inmem_fs.py:147`

### rmdir `def rmdir(self, path)`
- Defined: `fuse_inmem_fs.py:151`

### setxattr `def setxattr(self, path, name, value, options, position)`
- Defined: `fuse_inmem_fs.py:156`

### statfs `def statfs(self, path)`
- Defined: `fuse_inmem_fs.py:161`

### symlink `def symlink(self, target, source)`
- Defined: `fuse_inmem_fs.py:164`

### truncate `def truncate(self, path, length, fh)`
- Defined: `fuse_inmem_fs.py:172`

### unlink `def unlink(self, path)`
- Defined: `fuse_inmem_fs.py:178`

### utimens `def utimens(self, path, times)`
- Defined: `fuse_inmem_fs.py:182`

### write `def write(self, path, data, offset, fh)`
- Defined: `fuse_inmem_fs.py:188`

## getbanners.py

### slugify `def slugify(input)`
- Defined: `getbanners.py:54`

### main `def main(argc, argv)`
- Defined: `getbanners.py:58`
