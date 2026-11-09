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
    raise NotImplementedError("This function is not yet implemented.")
