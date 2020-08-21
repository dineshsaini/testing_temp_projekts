#!/usr/bin/env bash

inp="";
c="a";

for i in `seq 1 2500`; do
    inp="$inp$c";
    echo "trying with length: ${#inp}";
    nl="$(echo $inp | nc 10.10.10.6 666 | wc -l)"
    echo "got lines: $nl";
    if [[ $nl -lt 2 ]]; then
        echo "check string with length: ${#inp}, possible buffer overflow, recieved length $nl";
    fi;
done

