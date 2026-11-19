"""Test functionality of the account and transaction classes and their methods"""
from banking import Transaction

def test_transaction_class_exists():
    """Test that a transaction class exists"""
    transaction = Transaction(100)
    assert transaction

def test_transaction_class_stores_amount():
    """Transaction class stores the amount parameter"""
    transaction = Transaction(100)
    assert transaction.amount == 100