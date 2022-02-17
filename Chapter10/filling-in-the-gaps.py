#!/usr/bin/env python3
import shutil, os, re
from pathlib import Path

# get files with prefix in a sorted list
def getFiles(path, prefix):
    regex = re.compile(prefix+'(\d{1,})(.*)')
    fileList = sorted([file for file in os.listdir(path) if regex.match(file)])
    return fileList

def fillGaps(path, prefix):
    fileList = getFiles(path, prefix)
    regex = re.compile(prefix+'(\d{1,})(.*)')
    count = int(regex.search(fileList[0]).group(1))
    maxLength = len(regex.search(fileList[-1]).group(1))
    for file in fileList:
        mo = regex.search(file)
        if mo.group(1) != count:
            newFileName = prefix + str(count).rjust(maxLength, '0') + mo.group(2)
            shutil.move(Path(path) / file, Path(path) / newFileName)
        count += 1

def insertGaps(path, prefix, index):
    fileList = getFiles(path, prefix)
    regex = re.compile(prefix+'(\d{1,})(.*)')
    maxLength = len(regex.search(fileList[-1]).group(1))
    start = int(regex.search(fileList[0]).group(1))
    end = int(regex.search(fileList[-1]).group(1))
    if start <= index and index <= end:
        count = start
        i = 0
        while count < index:
            i += 1
            count = int(regex.search(fileList[i]).group(1))
        for file in fileList[:i:-1]:
            mo = regex.search(file)
            newFileNum = int(mo.group(1)) + 1
            newFileName = prefix + str(newFileNum).rjust(maxLength, '0') + mo.group(2)
            shutil.move(Path(path) / file, Path(path) / newFileName)
