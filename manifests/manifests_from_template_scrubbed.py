import os
import shutil

template = os.path.abspath('wintern_template')

serials = ''
serials = serials.split()

for serial in serials:
    shutil.copyfile(template, os.path.dirname(template) + '/' + serial)
