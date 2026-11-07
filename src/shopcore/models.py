from dataclasses import dataclass


@dataclass
class CartItem:
    price: float
    quantity: int
