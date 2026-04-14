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

    if not validate_ticket (code):
        raise ValueError ("Not a valid ticket code")

    first_digit = int(code [2])

    if 0 <= first_digit <= 3:
        return "General"
    elif 4 <= first_digit <= 6:
        return "VIP"
    elif 7 <= first_digit <= 9:
        return "Platinum"
    

def calculate_total(prices, discount = 0):
    pass
