from shopcore.models import CartItem


def calculate_total(items: list[CartItem]) -> float:
    total = 0

    for item in items:
        if item.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if item.price < 0:
            raise ValueError("Price cannot be negative")

        total += item.price * item.quantity

    return total
