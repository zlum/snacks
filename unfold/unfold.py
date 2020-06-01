#!/usr/bin/python3

# Usage: ./unfold.py text.txt | fold -w 80 -s | awk '{$1=$1};1'
 
import fileinput
import sys

paragraph = ''

for line in fileinput.input():
    line = line.strip()
    if not line:
        print(paragraph.rstrip(' '))
        paragraph = ''
        print(line)
        continue
    else:
        paragraph += line + ' '

if(paragraph):
    print(paragraph.rstrip(' '))
