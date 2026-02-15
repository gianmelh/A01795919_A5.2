"""
computeSales.py
Program to compute total sales from a price catalogue and a sales record.
"""

import sys
import json


def load_json_file(filepath: str):
    """Load JSON file safely."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{filepath}' is not valid JSON.")
    except OSError as error:
        print(f"Error reading file '{filepath}': {error}")
    return None


def compute_total_sales(price_data, sales_data):
    """Compute total sales based on catalogue and sales record."""
    total = 0.0

    # Convert catalogue to dictionary {product: price}
    price_dict = {}
    for item in price_data:
        product = item.get("title")
        price = item.get("price")

        if product is None or price is None:
            print("Warning: Invalid product in catalogue.")
            continue

        price_dict[product] = price

    # Process sales
    for sale in sales_data:
        product = sale.get("Product")
        quantity = sale.get("Quantity")

        if product not in price_dict:
            print(f"Warning: Product '{product}' not found in catalogue.")
            continue

        if not isinstance(quantity, (int, float)):
            print(f"Warning: Invalid quantity for '{product}'.")
            continue

        total += price_dict[product] * quantity

    return total


def main() -> None:
    """Main entry point."""
    if len(sys.argv) != 3:
        print(
             "Usage: python computeSales.py "
             "priceCatalogue.json salesRecord.json"
        )
        sys.exit(1)

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    price_data = load_json_file(price_file)
    sales_data = load_json_file(sales_file)

    if price_data is None or sales_data is None:
        sys.exit(1)

    total = compute_total_sales(price_data, sales_data)
    print(f"Total Sales: ${total:.2f}")


if __name__ == "__main__":
    main()
