from shopcore.discounts import apply_discount
from shopcore.models import CartItem
from shopcore.pricing import calculate_total
from shopcore.shipping import calculate_shipping_costs


def calculate_checkout_total(items, code):
    discounted_total = apply_discount(calculate_total(items), code)
    return discounted_total + calculate_shipping_costs(discounted_total)


def place_order(
    order: list[CartItem], inventory: dict[str, int], code: str = ""
) -> float:
    required_stock = {}
    for item in order:
        if item.quantity <= 0:
            raise ValueError("Order quantities must be positive")
        required_stock[item.sku] = required_stock.get(item.sku, 0) + item.quantity

    for sku, quantity in required_stock.items():
        if inventory.get(sku, 0) < quantity:
            raise ValueError(f"Insufficient stock for {sku}")

    total = calculate_checkout_total(order, code)

    for sku, quantity in required_stock.items():
        inventory[sku] -= quantity

    return total
