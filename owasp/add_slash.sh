#!/usr/bin/env bash

a=$1
echo $a | hexdump -e '/1 "\\x%02X"' | php addslash.php ;echo

echo $a | hexdump -e '/1 "0x%02X"' | php addslash.php ;echo
