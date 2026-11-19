"""Define the transaction and account classes and their methods"""
import datetime as dt

class Transaction:
    """A transaction class represents a monetary transaction event. It has two
    properties: an amount, and a timestamp."""

    def __init__(self,amount,timestamp=None):
        """Initialize transaction instances with an amount parameter"""
        self.amount = amount
        if timestamp is None:
            timestamp = dt.datetime.now()
        self.timestamp = timestamp

    def __repr__(self):
        """returns an expression which could be used to recreate this object"""
        return f'Transaction({self.amount},{repr(self.timestamp)})'

    def __str__(self) -> str:
        """returns a string including the timestamp and amount"""
        #check if the transaction is positive or negative
        sign = '+'
        if self.amount <0:
            sign = '-'

        #format string with date only and amount in common currency formatting
        return f'{self.timestamp.date()}: {sign}${abs(self.amount):,.2f}'

class Account():
    """The account class represents a bank account. It is constructed
    without any arguments."""

    def deposit(self,amount):
        return abs(amount)
