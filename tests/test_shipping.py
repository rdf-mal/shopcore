import pytest

from shopcore.shipping import calculate_shipping_costs


@pytest.mark.parametrize(
    "total_price, expected_cost",
    [
        (0, 0),
        (0.01, 4.90),
        (10, 4.90),
        (49.99, 4.90),
        (50, 0),
        (78.30, 0),
    ],
)
def test_calculate_shipping_costs(total_price, expected_cost):
    result = calculate_shipping_costs(total_price)
    assert result == pytest.approx(expected_cost), (
        "Shipping cost calculation is incorrect"
    )


def test_calculate_shipping_costs_negative_total():
    with pytest.raises(ValueError):
        calculate_shipping_costs(-10)
