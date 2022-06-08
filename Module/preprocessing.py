import re
from traceback import print_tb

def getDate(str):
    str = str.split('_')[-1]
    str = str.split('.')[0]
    return str