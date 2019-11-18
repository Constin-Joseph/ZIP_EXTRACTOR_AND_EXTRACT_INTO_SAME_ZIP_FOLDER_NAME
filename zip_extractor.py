import os
import glob
import zipfile

def extractor(b,c):
    dir_name_base = b
    dir_name_base1=c
    for arc_name in glob.iglob(os.path.join(dir_name_base, "*.zip")):
        arc_dir_name = os.path.splitext(os.path.basename(arc_name))[0]
        zf = zipfile.ZipFile(arc_name)
        zf.extractall(path=os.path.join(dir_name_base1, arc_dir_name))
        zf.close()
