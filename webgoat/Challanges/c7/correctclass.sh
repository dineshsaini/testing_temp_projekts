#!/usr/bin/env bash
classfname="$1"

if [ -z $classfname ]; then
    echo "classfile path/name needded"
    exit;
fi;

classname="$(echo $classfname | sed 's/\.class$//')"

cat $classfname| hexdump -e '16/1 "%02x " "\n"' -s 10 | xxd -r -p  > "$classname.1.class"
