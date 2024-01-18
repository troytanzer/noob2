#!/usr/bin/env python3

import os
import shutil
import glob
import subprocess
from os.path import join,dirname

def create_file_sizes(srcpath, destpath, newsize):
    # mogfrify will overwrite the file, but also doesn't ready everything into memory
    # at once, so we'll copy the orig, and then mogrify in the new dir
    if not os.path.exists(destpath):
        print(f'Creating directory {destpath}')
        os.makedirs(destpath)
    print('Copying original files over')
    for fname in glob.glob(os.path.join(srcpath, '*.jpg')):
        shutil.copy2(fname, os.path.abspath(destpath))
    print('Mogrify files in new path')
    # Adaptive resize does a slightly better job of resampling during the resize rather than -resize
    subprocess.run(['mogrify', '-adaptive-resize', newsize, os.path.join(destpath, '*.jpg')])
    print('All done!')

if __name__ == '__main__':
    # For quick test, assume the current dir is source, create subfolders and resize
    # Easiest to specify the full geometry as a string rather than x and y
    # Greater than sign indicates we only resize if it is larger than the size, otherwise
    # we leave alone (i.e. don't upscale).  Only really matters for the largest.
    create_file_sizes('.','./thumbs','200x200>')
    create_file_sizes('.','./medium','800x800>')
    create_file_sizes('.','./large','3000x3000>')