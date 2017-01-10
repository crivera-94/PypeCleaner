# Py Cleaner
#
# Name: Carlos Rivera
# Date: July 29, 2016

import os
from interface import *

# global dimensions
dimension = {
    'width': 500,
    'height': 400
}

# instantiate app and set window dimensions
pype_cleaner = SampleApp()
pype_cleaner.wm_title("Pype Cleaner")
pype_cleaner.geometry('{}x{}'.format(dimension['width'], dimension['height']))

pype_cleaner.mainloop()