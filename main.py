#import constants
#import tracker as tracker
import sys
from time import sleep
from rpi_lcd import LCD 


lcd = LCD()
for x in range(5):
    lcd.text('HOLY SHIT THIS IS AMAZING #:' + str(x +1), 1 , 'center')
    sleep(3) #Keep the text on screen for this many seconds
    lcd.clear() #clear the screen
    sleep(1)


