def calculate_shipping_costs(total_price: float) -> float:
    # Calculate shipping costs based on the total price of the order.
    if total_price < 0:
        raise ValueError("Total price cannot be negative")
    elif total_price < 50 and total_price > 0:
        return 4.90
    return 0
