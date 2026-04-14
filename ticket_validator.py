def validate_ticket (code):
    if not isinstance(code, str):
        raise TypeError ("Code must be a string")

    if len(code) != 8:
        return False

    if not code.startswith("TK"):
        return False

    if not code [2: ].isdigit():
        return False
    
    return True


def get_ticket_tier (code):
    pass

def calculate_total(prices, discount = 0):
    pass
