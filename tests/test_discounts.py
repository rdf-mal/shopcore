import pytest

from shopcore.discounts import apply_discount


@pytest.mark.parametrize(
    "total, expected",
    [
        (100, 90),
        (35, 31.50),
        (41.99, 37.791),
        (0, 0),
    ],
)
def test_apply_discount(total, expected):
    result = apply_discount(total, "SAVE10")
    assert result == pytest.approx(expected), "Discount not applied correctly"


@pytest.mark.parametrize(
    "code",
    [
        "SAVE10",
        "save10",
        "SaVe10",
        "saVE10",
    ],
)
def test_apply_discount_case_insensitive(code):
    result = apply_discount(100, code)
    assert result == 90, "Discount code should be case-insensitive"


def test_apply_discount_invalid_code():
    result = apply_discount(100, "INVALID10")
    assert result == 100, "Invalid discount code should not change total"


def test_apply_discount_negative_total():
    with pytest.raises(ValueError):
        apply_discount(-100, "SAVE10")
