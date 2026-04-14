import pytest
from ticket_validator import *

@pytest.mark.parametrize ("code, expected", [
    ("TK123456", True)
    ("TK329503", True)
    ("TKS$4523", False)
    ("TX123456", False)
])

def test_validate_ticket_valid_cases (code, expected):
    assert validate_ticket(code) == expected

def test_validate_ticket_type_error ():
    with pytest.raises(TypeError):
        validate_ticket(12345678)

@pytest.mark.parametrize ("code, expected", [
    ("TK123456", "General")
    ("TK524325", "VIP")
    ("TK712397", "Platinum")
])

def test_get_ticket_tier_valid (code, expected):
    assert get_ticket_tier(code) == expected

def test_get_ticket_tier_invalid ():
    with pytest.raises(ValueError):
        get_ticket_tier(TKS14050)

def test_calculate_total_basic ():
    assert calculate_total([10.0, 20.0], 0.1) == 27.0

def test_calculate_total_empty():
    assert calculate_total([])

def test_calculate_total_fail_value_err ():
    with pytest.raises (ValueError):
        calculate_total("not a list")

def test_calculate_total_discount_range ():
    with pytest.raises (TypeError):
        calculate_total([15.0], 1.5)