#!/usr/bin/env python3
# selective-copy.py - walks through a filder tree and searches for files
# with a certain file extension and copies them in to a new folder
import shutil, os, re, sys
from pathlib import Path

def selectiveCopy(source, destination, extension):
    regex = re.compile(extension)
    for foldername, subfolders, filenames in os.walk(source):
        for filename in filenames:
            if Path(filename).suffix == extension:
                print(f'Copying {filename} from {foldername} to {destination}')
                shutil.copy(Path(foldername) / filename, destination)

if len(sys.argv) == 4:
    source, destination, extension = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]  
    if source.exists() and destination.exists():
        selectiveCopy(source, destination, extension)
    else:
        print("Error: invalid path.")
else:
    print("Usage: ./selective-copy.py <source> <destination> <extension>")
