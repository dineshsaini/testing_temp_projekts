#!/usr/bin/env bash
hx=$(hexdump -v -e '1/1 "%02x" " "' $1)
echo " $hx" | sed 's/ /%/g' | sed 's/%$//'
