"""
computeSales.py

Program to compute total sales from a price catalogue and a sales record.
"""

import sys


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

    print(f"Price file: {price_file}")
    print(f"Sales file: {sales_file}")


if __name__ == "__main__":
    main()
