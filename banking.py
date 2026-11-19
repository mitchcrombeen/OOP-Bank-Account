"""Define the transaction and account classes and their methods"""

class Transaction:
    def __init__(self,amount,timestamp=None):
        """Initialize transaction instances with an amount parameter"""
        self.amount = amount
        self.timestamp = timestamp
