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

    print("Files loaded successfully.")


if __name__ == "__main__":
    main()
