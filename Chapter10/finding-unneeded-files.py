#!/usr/bin/env python3
import os, sys

def printBigFiles(path, file):
    try:
        p = os.path.join(path, file)
        fileSize = os.path.getsize(p)
        if fileSize > 100000000:
            print(f'{fileSize//100}MB: {p}')
    except FileNotFoundError:
        pass

def findUnneededFiles(path):
    for foldername, subfolders, filenames in os.walk(path):
        for subfolder in subfolders:
            printBigFiles(foldername, subfolder)
        for filename in filenames:
            printBigFiles(foldername, filename)

if len(sys.argv) == 2:
    findUnneededFiles(sys.argv[1])
