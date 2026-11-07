import pytest

from shopcore.pricing import calculate_total


def test_calculate_total():

    items = [
        {"price": 10, "quantity": 2},
        {"price": 5, "quantity": 3},
    ]

    result = calculate_total(items)

    assert result == 35


def test_empty_card():
    items = []

    result = calculate_total(items)

    assert result == 0


def test_negative_quantity_is_rejected():
    items = [{"price": 10, "quantity": -2}]

    with pytest.raises(ValueError):
        calculate_total(items)


def test_negative_price_is_rejected():
    items = [{"price": -10, "quantity": 2}]

    with pytest.raises(ValueError):
        calculate_total(items)
