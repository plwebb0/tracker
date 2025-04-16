from pathlib import Path
import csv
from datetime import date
import sys
import platform
from . import constants


p = sys.argv[0]
dict={}
for argcount, argument in enumerate(sys.argv):
    dict['p{0}'.format(argcount)] = argument

p = dict['p2']
m = dict['p3']
e = dict['p4']


def getFilePath():
    os = platform.system()
    if os == 'Windows':
        filepath = constants.WINDOWS_LOGFILE_PATH
    elif os == 'Linux': 
        filepath = constants.LINUX_LOGFILE_PATH
    else: raise Exception("Not Windows or Linux I wasn't prepared for this")
    return filepath


def grocerylog(price, market, buyer):    
    fieldDict = {'price':price,'market':market,'date':constants.TODAY,'buyer':buyer}
    #new_row = [price,market,today,buyer]

    if Path(getFilePath).exists():
        with open(getFilePath,newline='') as csvfile:
            grocfile = list(csv.reader(csvfile,delimiter=',',quotechar='"'))   
            for row in grocfile:
                print(row)
            csvfile.close()
            
        with open(getFilePath,'a',newline='') as csvfile:
            fieldnames = ['price','market','date','buyer']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(fieldDict)
    else:
        raise Exception("Grocery Log file not found.")

grocerylog(p,m,e)