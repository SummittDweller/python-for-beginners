# Find all mp3 files
# This script will search for *.mp3 files from the hardcoded rootPath.  It will report all found and remove or rename
# the smaller of two files if the difference in size is less than 1% of the found file.

import fnmatch
import os
import re

rootPath = '/'
rootPath = '/Volumes/files/STORAGE/_AUDIO'

pattern = '*.mp3'
pattern = '*1).mp3'

count = 0
actions = 0

for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):

        # Retrieve and report information about the found file.
        count += 1
        fullFilename = os.path.join(root, filename)
        fileSize = os.path.getsize(fullFilename)
        print "The full file name is " + fullFilename + " with a size of " + str(fileSize) + " bytes."

        # Retrieve information about the corresponding 'original', unnumbered file.
        orgFilename = re.sub(r' \(\d*\).mp3', '.mp3', filename)
        orgFullFilename = os.path.join(root, orgFilename)
        orgFileSize = os.path.getsize(orgFullFilename)
        print "   The original full file name is " + orgFullFilename + " with a size of " + str(orgFileSize) + " bytes."

        # Find the path to the corresponding artist.
        artistPath = os.path.realpath(root+'/..')
        print "   The artist path is " + artistPath + "."

        # Calculate and report the % difference in size.
        difference = int((float(orgFileSize) - float(fileSize)) / float(fileSize) * 100.0)
        print "    The difference in sizes is " + str(difference) + " percent of the found file size."

        # If there is a significant difference in size (more than +/- 1%) report it and do nothing else.
        if (abs(difference) > 1):
            print ">>>>>>>>>>>>>> There's a significant difference in these files! <<<<<<<<<<<<<<<"

        # If the found file size <= original file size, remove it.  If not, remove the original and rename the found file.
        elif fileSize <= orgFileSize:
            print ">>>>> Removing " + fullFilename + "!"
            os.remove(fullFilename)
            actions += 1
        else:
            print ">>>>>>>>>>>>> Renaming " + fullFilename + " to " + orgFullFilename + "!"
            os.remove(orgFullFilename)
            os.rename(fullFilename, orgFullFilename)
            actions += 1

print " "
print "There were " + str(count) + " files matching the '" + str(pattern) + "' pattern."
print "   " + str(actions) + " were removed."
