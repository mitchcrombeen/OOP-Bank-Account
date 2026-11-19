"""Define the transaction and account classes and their methods"""
import datetime as dt

class Transaction:
    def __init__(self,amount,timestamp=None):
        """Initialize transaction instances with an amount parameter"""
        self.amount = amount
        if timestamp is None:
            timestamp = dt.datetime.now()
        self.timestamp = timestamp

    def __repr__(self):
        """returns an expression which could be used to recreate this object"""
        return f'Transaction({self.amount},{repr(self.timestamp)})'
