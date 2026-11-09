from dataclasses import dataclass


@dataclass
class CartItem:
    sku: str
    price: float
    quantity: int
