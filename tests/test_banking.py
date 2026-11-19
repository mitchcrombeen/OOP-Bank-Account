"""Test functionality of the account and transaction classes and their methods"""

import datetime as dt
from banking import Transaction
from banking import Account


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

def test_transaction_has_a_repr_method_that_returns_an_appropriate_str():
    """__repr__ returns a string that could be used to create a similar transaction"""
    transaction = Transaction(100,dt.datetime(2026,11,19))

    #created on separate line do to the length of text
    expected_output = 'Transaction(100,datetime.datetime(2026, 11, 19, 0, 0))'

    assert repr(transaction) == expected_output

def test_transaction_has_str_method_which_returns_string_with_amount_and_timestamp():
    """test that Transaction has a __str__ method which returns a string
    containing the timestamp and amount"""
    transaction = Transaction(1000000, dt.datetime(2026, 11, 19))

    expected_output = '2026-11-19: +$1,000,000.00'

    assert str(transaction) == expected_output

def test_transaction_str_method_can_represent_negative_amounts():
    """Test that when __str__ is called on a negative amount, the sign change is
    reflected in the output string"""

    uhoh = Transaction(-1000000, dt.datetime(2026, 11, 19))

    expected_output = '2026-11-19: -$1,000,000.00'

    assert str(uhoh) == expected_output

def test_deposit_converts_amount_to_positive_value():
    account = Account()

    assert account.deposit(-1) == 1

