import pytest
import func

def test_reformat_date():
    assert func.reformat_date('2018-07-11T02:26:18.671407') == "11-7-2018"


def test_reformat_card_number():
    assert func.reformat_card_number("1234567891234567") == "1234 56** **** 4567"


def test_reformat_card_name():
    assert func.reformat_card_name("Счет") == "Счет"
    assert func.reformat_card_name("Visa Classic") == "Visa Classic"


def test_reformat_invoice():
    assert func.reformat_invoice("72082042523231456215") == "**6215"


def test_reformat_invoice_name():
    assert func.reformat_invoice_name("Счет") == "Счет"
    assert func.reformat_invoice_name("Visa Classic") == "Visa Classic"