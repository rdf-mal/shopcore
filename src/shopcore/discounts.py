def apply_discount(total, code):
    if total < 0:
        raise ValueError("Total cannot be negative")
    code = code.casefold()
    # Normalize the code to lowercase for case-insensitive comparison
    if code == "save10":
        return total * 0.9  # Apply a 10% discount
    return total  # Return the original total if the code is invalid
