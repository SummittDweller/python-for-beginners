import os
files = os.listdir('.')
for f in files:
    path, ext = os.path.splitext(f)
    if ext.isupper():
        os.rename(f, path + ext.lower())
