"""Test functionality of the account and transaction classes and their methods"""
from banking import Transaction
import datetime as dt


def test_transaction_class_stores_amount():
    """Transaction class stores the amount parameter"""
    transaction = Transaction(100)
    assert transaction.amount == 100

def test_transaction_has_optional_timestamp_parameter():
    """Transaction class can be initialized with a second parameter, timestamp"""
    transaction = Transaction(100,dt.datetime(1999,12,31))
    assert transaction.timestamp == dt.datetime(1999,12,31)

def test_transaction_uses_current_datetiime_if_none_is_provided():
    """If no timestamp is given, uses the current datetime"""
    #check time before initializing the transaction
    time_before = dt.datetime.now()

    transaction = Transaction(100)

    #check time after initializing the transaction
    time_after = dt.datetime.now()

    assert time_before <= transaction.timestamp <= time_after