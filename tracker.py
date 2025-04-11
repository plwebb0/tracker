from pathlib import Path
import csv
from datetime import date
import sys

p = sys.argv[0]

dict={}
for argcount, argument in enumerate(sys.argv):
    dict['p{0}'.format(argcount)] = argument

p = dict['p2']
m = dict['p3']
e = dict['p4']
today = date.today().isoformat()



def grocerylog(price, market, buyer):

    glog = Path('C:/Users/plweb/Documents/grocerylog.csv')
    logpath = 'C:/Users/plweb/Documents/grocerylog.csv'
    today = date.today().isoformat()
    fieldDict = {'price':price,'market':market,'date':today,'buyer':buyer}
    #new_row = [price,market,today,buyer]

    if glog.exists():
        with open(logpath,newline='') as csvfile:
            grocfile = list(csv.reader(csvfile,delimiter=',',quotechar='"'))
            
            for row in grocfile:
                print(row)
            csvfile.close()
            
        with open(logpath,'a',newline='') as csvfile:
            fieldnames = ['price','market','date','buyer']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(fieldDict)
    else:
        raise Exception("Grocery Log file not found.")

grocerylog(p,m,e)