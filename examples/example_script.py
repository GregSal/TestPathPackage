# -*- coding: utf-8 -*-
'''
Test path and other package environment settings

Created on Thu Mar  3 07:54:12 2022

@author: smoke
'''


from pathlib import Path
import sys

print(f'In module: {__name__}')
print(f'current path is: {Path.cwd()}\n')

print('PythonPaths:')
for path_str in sys.path:
    print(f'\t{path_str}')

# %% Import function from module in src
from simple_script import what_is_tomorrow

tomorrow = what_is_tomorrow()
tomorrow_str = tomorrow.strftime("%A, %d. %B %Y %I:%M%p")
print(f'Tomorrow is: {tomorrow_str}')

# %% Import numpy module
import numpy as np
num_list = np.arange(1,5)
print(num_list)

# %% Import sub-module
from addition.extra_script import build_array
num_ary = build_array(5)
print(num_ary)

# %% Exiting module
print(f'\nDone module: {__name__}\n\n')
