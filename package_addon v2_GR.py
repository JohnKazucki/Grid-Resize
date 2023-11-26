import shutil
import os


# setup variables

ADDON_PATH = "D:/Blender/_GIT_addon/Grid-Resize/Grid_Resizer"
PACKAGE_PATH = "D:/Blender/_GIT_addon/Grid-Resize/autobuild"

# clean up any __pycache folders in the directory
# from https://stackoverflow.com/questions/63712737/how-to-delete-all-pycache-folders-in-directory-tree
for directories, subfolder, files in os.walk(ADDON_PATH):
    if os.path.isdir(directories):
        if directories[::-1][:11][::-1] == '__pycache__':
                        shutil.rmtree(directories)

# find name of the addon folder
name = ADDON_PATH.split("/")
name = name[-1]

# get version number, WARNING : there can be NO BPY IMPORT in the __init__.py file!!!
# from https://www.geeksforgeeks.org/python-import-module-outside-directory/
import sys       
sys.path.insert(1, ADDON_PATH)
from __init__ import bl_info
version = bl_info["version"]

ADDON_VERSION = "v" + str(version[0]) + "." + str(version[1]) + "." + str(version[2])

# thanks to https://stackoverflow.com/questions/32640053/compressing-directory-using-shutil-make-archive-while-preserving-directory-str
# for this
def make_archive(source, destination):
    base_name = '.'.join(destination.split('.')[:-1])
    format = destination.split('.')[-1]
    root_dir = os.path.dirname(source)
    base_dir = os.path.basename(source.strip(os.sep))
    shutil.make_archive(base_name, format, root_dir, base_dir)

# package the addon folder into a .zip
zipname = name+ " " + ADDON_VERSION+".zip"
make_archive(ADDON_PATH, PACKAGE_PATH+"/"+zipname)
