from pathlib import path
import csv
from datetime import date

class LogHandler:
    def grocerylog(self, price, market,buyer):

        p = path('.Documents/grocerylog.csv')
        today = date.today().isoformat()
        if p.exists():
            with open('grocerylog.csv',newline='') as csvfile:
                fieldnames = ['price','market','date','buyer']
                writer = csv.DictWriter(grocerylog.csv, fieldnames=fieldnames)
                writer.writeheader():
                writer.writerow({'price':price,'market':market,'date':today,'buyer':buyer})
        else:
            raise Exception("Grocery Log file not found.")

        