def calculate_total(items: list) -> float:
    total = 0

    for item in items:
        if item.get("quantity") < 0:
            raise ValueError("Quantity cannot be negative")
        if item.get("price") < 0:
            raise ValueError("Price cannot be negative")

        total += item.get("price") * item.get("quantity")

    return total
