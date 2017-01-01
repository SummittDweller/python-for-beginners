import os
dir = "."
cpt = sum([len(files) for r, d, files in os.walk(dir)])
print "The total file count in directory '" + dir "' is: " + str(cpt) + "."
