# Coverage Report

====================================================================== tests coverage =======================================================================
______________________________________________________ coverage: platform linux, python 3.12.1-final-0 ______________________________________________________

Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
ticket_validator.py      30      2    93%   6, 20
---------------------------------------------------
TOTAL                    30      2    93%
================================================================== short test summary info ==================================================================
FAILED test_ticket_validator.py::test_get_ticket_tier_invalid - NameError: name 'TK124500' is not defined
FAILED test_ticket_validator.py::test_calculate_total_empty - ValueError: Can not have an empty price list
FAILED test_ticket_validator.py::test_calculate_total_fail_value_err - TypeError: Prices must be a list
FAILED test_ticket_validator.py::test_calculate_total_discount_range - ValueError: Can not have a discount value below 0, or higher than 1
================================================================ 4 failed, 9 passed in 0.21s ================================================================
