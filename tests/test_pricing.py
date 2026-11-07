import pytest

from shopcore.models import CartItem
from shopcore.pricing import calculate_total


def test_calculate_total():

    items = [
        CartItem(price=10, quantity=2),
        CartItem(price=5, quantity=3),
    ]

    result = calculate_total(items)

    assert result == 35


def test_empty_card():
    items = []

    result = calculate_total(items)

    assert result == 0


def test_negative_quantity_is_rejected():
    items = [CartItem(price=10, quantity=-2)]

    with pytest.raises(ValueError):
        calculate_total(items)


def test_negative_price_is_rejected():
    items = [CartItem(price=-10, quantity=2)]

    with pytest.raises(ValueError):
        calculate_total(items)


@pytest.mark.parametrize(
    "price, quantity, expected",
    [
        (10, 2, 20),
        (5, 3, 15),
        (0, 10, 0),
        (2.5, 4, 10),
    ],
)
def test_item_subtotal(price, quantity, expected):

    cart = [CartItem(price=price, quantity=quantity)]

    assert price * quantity == expected
    assert calculate_total(cart) == expected


@pytest.mark.parametrize(
    "items, expected",
    [
        ([(10, 2), (5, 3)], 35),
        ([(0, 10), (2.5, 4)], 10),
        ([(100, 1), (50, 2)], 200),
        ([(1.5, 4), (1, 5), (2, 2)], 15),
        ([(0, 0), (0, 0)], 0),
    ],
)
def test_valid_carts(items, expected):
    card = [CartItem(price=price, quantity=quantity) for price, quantity in items]

    assert calculate_total(card) == expected
