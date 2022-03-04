# -*- coding: utf-8 -*-
'''
Test path and other package environment settings

Created on Thu Mar  3 07:54:12 2022

@author: Greg Salomons
'''

from pathlib import Path
import sys
from datetime import datetime
import parsedatetime


### Status Print Statements ###
print(f'\nIn module: {__name__}\n')
print(f'current path is: {Path.cwd()}\n')

print('PythonPaths:')
for path_str in sys.path:
    print(f'\t{path_str}')


### Functions for testing ###


def what_is_tomorrow():
    cal = parsedatetime.Calendar()
    time_struct, parse_status = cal.parse("tomorrow")
    return datetime(*time_struct[:6])

def main():
    cal = parsedatetime.Calendar()
    yesterday, parse_status = cal.parse("yesterday")
    yesterday_dt = datetime(*yesterday[:6])
    yesterday_str = yesterday_dt.strftime("%A, %d. %B %Y")
    print(f'Yesterday is: {yesterday_str}')

if __name__ == '__main__' :
    main()


print(f'\nDone module: {__name__}\n\n')
