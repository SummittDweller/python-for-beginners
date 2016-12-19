# Find all mp3 files
# This script will search for *.mp3 files from the rootPath ("/")

import fnmatch
import os
 
rootPath = '/'
pattern = '*.mp3'
 
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))
