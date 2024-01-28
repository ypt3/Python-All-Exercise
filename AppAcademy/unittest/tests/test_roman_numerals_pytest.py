import pytest
from app.roman_numerals import parse

@pytest.mark.parametrize("input,expected",[("IX", 9), ("X", 10)])
def test_roman_numeral_parser(input,expected):
    value = parse(input)
    assert value == expected

def test_xi():
    assert parse("XI") == 11

def test_xiv():
    assert parse("XIV") == 14

def test_mccclxxxiii():
    assert parse("MCCCLXXXIII") == 1383

