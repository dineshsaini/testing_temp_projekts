#!/usr/bin/env bash

cat $1 | tr '\n' ' ' | sed 's/ \+/ /g' | hexdump -e '2/1 "%02X"' | tr '*\n' ' ' | sed 's/ \+//g' > hex_exec_cmd.php
