#!/usr/bin/env bash
hexdump -v -e '/1 "%02x" " "' $1 | sed 's/ /\\x/g' |sed 's/\\x$//' | sed 's/^/\\x/'

echo;
