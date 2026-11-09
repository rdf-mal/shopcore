import pytest

from shopcore.checkout import calculate_checkout_total, place_order
from shopcore.models import CartItem


@pytest.fixture
def sample_cart():
    return [
        CartItem(sku="item-1", price=10, quantity=2),
        CartItem(sku="item-2", price=5, quantity=3),
    ]


def test_checkout_with_discount(sample_cart):
    assert calculate_checkout_total(sample_cart, "SAVE10") == pytest.approx(36.40)

    sample_cart.append(CartItem(sku="item-3", price=20, quantity=1))
    assert calculate_checkout_total(sample_cart, "SAVE10") == pytest.approx(54.40)


def test_checkout_without_discount(sample_cart):
    assert calculate_checkout_total(sample_cart, "") == pytest.approx(39.90)
    assert calculate_checkout_total(sample_cart, "UNKNOWN") == pytest.approx(39.90)

    sample_cart.append(CartItem(sku="item-3", price=20, quantity=1))
    assert calculate_checkout_total(sample_cart, "") == pytest.approx(55)


def test_checkout_with_discount_and_shipping():
    items = [CartItem(sku="item-1", price=50, quantity=1)]

    assert calculate_checkout_total(items, "SAVE10") == pytest.approx(49.90)


def test_checkout_with_discount_and_free_shipping():
    items = [CartItem(sku="item-1", price=60, quantity=1)]

    assert calculate_checkout_total(items, "SAVE10") == pytest.approx(54)


def test_checkout_with_empty_cart():
    assert calculate_checkout_total([], "SAVE10") == 0


@pytest.mark.parametrize(
    "item",
    [
        CartItem(sku="item-1", price=-10, quantity=1),
        CartItem(sku="item-1", price=10, quantity=-1),
    ],
)
def test_checkout_rejects_invalid_items(item):
    with pytest.raises(ValueError):
        calculate_checkout_total([item], "SAVE10")


def test_place_order_accepts_available_items_and_calculates_checkout_total():
    order = [CartItem(sku="shirt", price=60, quantity=1)]
    inventory = {"shirt": 2}

    result = place_order(order, inventory, "SAVE10")

    assert result == pytest.approx(54)
    assert inventory == {"shirt": 1}


def test_place_order_rejects_quantity_above_stock_without_changing_inventory():
    order = [CartItem(sku="shirt", price=20, quantity=3)]
    inventory = {"shirt": 2}

    with pytest.raises(ValueError):
        place_order(order, inventory)

    assert inventory == {"shirt": 2}


@pytest.mark.parametrize("quantity", [0, -1])
def test_place_order_rejects_non_positive_quantity_without_changing_inventory(quantity):
    order = [CartItem(sku="shirt", price=20, quantity=quantity)]
    inventory = {"shirt": 2}

    with pytest.raises(ValueError):
        place_order(order, inventory)

    assert inventory == {"shirt": 2}


def test_place_order_rejects_entire_order_if_one_item_is_unavailable():
    order = [
        CartItem(sku="shirt", price=20, quantity=1),
        CartItem(sku="hat", price=10, quantity=2),
    ]
    inventory = {"shirt": 3, "hat": 1}

    with pytest.raises(ValueError):
        place_order(order, inventory)

    assert inventory == {"shirt": 3, "hat": 1}


def test_place_order_counts_repeated_skus_together():
    order = [
        CartItem(sku="shirt", price=20, quantity=1),
        CartItem(sku="shirt", price=20, quantity=1),
    ]
    inventory = {"shirt": 1}

    with pytest.raises(ValueError):
        place_order(order, inventory)

    assert inventory == {"shirt": 1}
