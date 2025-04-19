import tracker
import lcd
import constants
import sys

p = sys.argv[0]
dict={}
for argcount, argument in enumerate(sys.argv):
    dict['p{0}'.format(argcount)] = argument

p = dict['p2']
m = dict['p3']
e = dict['p4']





main(p,m,e)