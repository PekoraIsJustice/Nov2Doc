import os
import fnmatch
from Module import preprocessing

def chkUpdate(cur, path, title):
    pre = '00000000'
    date = fnmatch.filter(os.listdir(path), title+'*.docx')
    if len(date) != 0:
        pre = preprocessing.getDate(date[0])
    if cur == pre : return True 
    else : return False