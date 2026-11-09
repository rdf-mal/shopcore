import pytest

from shopcore.discounts import apply_discount


def rest_apply_discount():
    result = apply_discount(100, "SAVE10")
    assert result == 90, "Discount code should be case-insensitive"


def test_apply_discount_lowercase_code():
    result = apply_discount(100, "save10")
    assert result == 90, "Discount code should be case-insensitive"


def test_apply_discount_mixedcase_code():
    result = apply_discount(100, "SaVe10")
    assert result == 90, "Discount code should be case-insensitive"


def test_apply_discount_zero_total():
    result = apply_discount(0, "SAVE10")
    assert result == 0, "Discount on zero total should remain zero"


def test_apply_discount_invalid_code():
    result = apply_discount(100, "INVALID10")
    assert result == 100, "Invalid discount code should not change total"


def test_apply_discount_negative_total():
    with pytest.raises(ValueError):
        apply_discount(-100, "SAVE10")
