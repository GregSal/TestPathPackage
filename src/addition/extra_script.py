# -*- coding: utf-8 -*-
'''
Test path and other package environment settings

Created on Thu Mar  3 07:54:12 2022

@author: Greg Salomons
'''

from pathlib import Path
import sys
from datetime import datetime
from pprint import pprint

import parsedatetime
import numpy as np


### Status Print Statements ###
print(f'\nIn module: {__name__}\n')
print(f'current path is: {Path.cwd()}\n')

print('PythonPaths:')
for path_str in sys.path:
    print(f'\t{path_str}')


### Functions for testing ###
def build_array(size: int = 2) -> np.ndarray:
    a_range = range(1, size + 1)
    ary = np.array(a_range, dtype=np.uint32)
    return ary


def main():
    ary = build_array(10)
    pprint(ary)

if __name__ == '__main__' :
    main()


print(f'\nDone module: {__name__}\n\n')
