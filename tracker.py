from pathlib import path

class LogHandler:
    def grocerylog(price, market):
        p = path('.Documents/grocerylog.csv')
        if p.exists():
            p.open()
        else:
            raise Exception("Grocery Log file not found.")