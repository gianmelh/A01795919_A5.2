from src.compute_sales import compute_total_sales


def test_compute_total_sales_basic():
    price_data = [
        {"title": "Apple", "price": 10.0},
        {"title": "Banana", "price": 5.0},
    ]

    sales_data = [
        {"Product": "Apple", "Quantity": 2},
        {"Product": "Banana", "Quantity": 3},
    ]

    result = compute_total_sales(price_data, sales_data)

    assert result == 35.0


def test_product_not_in_catalogue():
    price_data = [{"title": "Apple", "price": 10.0}]
    sales_data = [{"Product": "Orange", "Quantity": 5}]

    result = compute_total_sales(price_data, sales_data)

    assert result == 0.0


def test_invalid_quantity():
    price_data = [{"title": "Apple", "price": 10.0}]
    sales_data = [{"Product": "Apple", "Quantity": "two"}]

    result = compute_total_sales(price_data, sales_data)

    assert result == 0.0
