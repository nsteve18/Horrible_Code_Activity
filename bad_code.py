"""
BAD CODE DEMONSTRATION
Selected Violations:
1. DRY (Don't Repeat Yourself) - Copy-pasted calculation logic and formatting across functions.
2. Single Responsibility Principle (SRP) - Functions mix input parsing, math, business logic, and UI formatting.
3. YAGNI (You Aren't Gonna Need It) - Unnecessary over-engineering with unused speculative classes and interfaces.
4. Poor Documentation & Clean Code - Cryptic variable names, misleading comments, and dead code.
"""

import math


# --- YAGNI VIOLATION: Over-engineered speculative architecture for a simple cart ---
class AbstractCurrencyExchangeManagerFactoryInterface:
    def __init__(self):
        # Speculative feature for future crypto/forex integration
        self.crypto_rates = {"BTC": 0.000015, "ETH": 0.00035}
        self.inflation_adjustment_index = 1.025
        self.unused_buffer = []

    def convert_to_bitcoin(self, amount):
        return amount * self.crypto_rates["BTC"]

    def calculate_predictive_inflation(self, amount, years):
        return amount * (self.inflation_adjustment_index ** years)


# --- SRP & DRY VIOLATIONS: Monolithic functions with duplicated logic ---
def process_grocery_cart(items):
    # Cryptic variables
    s = 0
    # Duplicated subtotal calculation
    for item in items:
        price = item[1]
        qty = item[2]
        s = s + (price * qty)  # adding price times quantity to s

    # Misleading comment: says 5% discount, actually calculates 10%
    # DRY violation: Copy-pasting discount logic
    disc = 0
    if s > 100:
        disc = s * 0.10  # 5% discount applied here

    sub_after_disc = s - disc

    # DRY violation: Copy-pasting tax calculation logic (8% tax)
    tax = sub_after_disc * 0.08
    tot = sub_after_disc + tax

    # SRP violation: Function handles calculations AND UI output directly
    print("========================================")
    print("           GROCERY RECEIPT              ")
    print("========================================")
    for i in items:
        print(i[0] + " x" + str(i[2]) + " @ $" + str(i[1]) + " = $" + str(i[1] * i[2]))
    print("----------------------------------------")
    print("Subtotal: $" + str(s))
    print("Discount: -$" + str(disc))
    print("Tax (8%): $" + str(tax))
    print("TOTAL DUE: $" + str(tot))
    print("========================================\n")


def process_electronics_cart(items):
    # DRY violation: Exactly the same subtotal loop duplicated from groceries
    s = 0
    for item in items:
        p = item[1]
        q = item[2]
        s = s + (p * q)

    # DRY violation: Duplicated discount logic with subtle hardcoded changes
    disc = 0
    if s > 100:
        disc = s * 0.10

    sub_after_disc = s - disc

    # Electronics has a different hardcoded tax rate embedded inside receipt generator
    tax = sub_after_disc * 0.15
    tot = sub_after_disc + tax

    # SRP violation: Duplicated formatting and printing logic
    print("========================================")
    print("         ELECTRONICS RECEIPT            ")
    print("========================================")
    for item in items:
        print(item[0] + " x" + str(item[2]) + " @ $" + str(item[1]) + " = $" + str(item[1] * item[2]))
    print("----------------------------------------")
    print("Subtotal: $" + str(s))
    print("Discount: -$" + str(disc))
    print("Tax (15%): $" + str(tax))
    print("TOTAL DUE: $" + str(tot))
    print("========================================\n")


def main():
    grocery_items = [("Apples", 2.50, 4), ("Milk", 3.99, 2), ("Cereal", 5.00, 3)]
    electronics_items = [("Headphones", 89.99, 1), ("USB Cable", 12.50, 2)]

    # Instantiating unused over-engineered factory
    factory = AbstractCurrencyExchangeManagerFactoryInterface()

    process_grocery_cart(grocery_items)
    process_electronics_cart(electronics_items)


if __name__ == "__main__":
    main()