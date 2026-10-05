"""
GOOD CODE DEMONSTRATION
Best Practices Implemented:
1. DRY (Don't Repeat Yourself) - Calculation logic and formatting are centralized into reusable functions.
2. Single Responsibility Principle (SRP) - Core logic, tax/discount calculation, and UI presentation are cleanly separated.
3. YAGNI (You Aren't Gonna Need It) - Removed unused classes, predictive models, and speculative features.
4. Clean Code & Documentation - Meaningful variable names, PEP 8 compliance, explicit type hints, and accurate docstrings.
"""

from typing import List, Tuple

# Type alias for clarity: (item_name, unit_price, quantity)
CartItem = Tuple[str, float, int]


# --- CORE CALCULATION FUNCTIONS (Single Responsibility: Math only) ---

def calculate_subtotal(items: List[CartItem]) -> float:
    """Calculates the total cost of items before taxes or discounts."""
    return sum(price * quantity for _, price, quantity in items)


def calculate_discount(subtotal: float, threshold: float = 100.0, discount_rate: float = 0.10) -> float:
    """Applies a percentage discount if the subtotal exceeds the threshold."""
    if subtotal >= threshold:
        return subtotal * discount_rate
    return 0.0


def calculate_tax(amount: float, tax_rate: float) -> float:
    """Calculates sales tax based on a given tax rate."""
    return amount * tax_rate


# --- PRESENTATION / FORMATTING FUNCTIONS (Single Responsibility: UI Output) ---

def format_receipt(category_name: str, items: List[CartItem], tax_rate: float) -> str:
    """
    Generates a formatted text receipt for a given cart and tax rate.
    Reuses core calculation functions to maintain DRY principles.
    """
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    taxable_amount = subtotal - discount
    tax = calculate_tax(taxable_amount, tax_rate)
    total = taxable_amount + tax

    lines = [
        "========================================",
        f"           {category_name.upper()} RECEIPT",
        "========================================"
    ]

    for name, price, qty in items:
        item_total = price * qty
        lines.append(f"{name:<18} x{qty:<2} @ ${price:>6.2f} = ${item_total:>7.2f}")

    lines.extend([
        "----------------------------------------",
        f"Subtotal:           ${subtotal:>8.2f}",
        f"Discount:          -${discount:>8.2f}",
        f"Tax ({tax_rate * 100:>2.0f}%):          ${tax:>8.2f}",
        f"TOTAL DUE:          ${total:>8.2f}",
        "========================================\n"
    ])

    return "\n".join(lines)


def main() -> None:
    # Sample data
    grocery_items: List[CartItem] = [("Apples", 2.50, 4), ("Milk", 3.99, 2), ("Cereal", 5.00, 3)]
    electronics_items: List[CartItem] = [("Headphones", 89.99, 1), ("USB Cable", 12.50, 2)]

    # Tax rates
    GROCERY_TAX_RATE = 0.08
    ELECTRONICS_TAX_RATE = 0.15

    # Process and display receipts cleanly
    print(format_receipt("Grocery", grocery_items, GROCERY_TAX_RATE))
    print(format_receipt("Electronics", electronics_items, ELECTRONICS_TAX_RATE))


if __name__ == "__main__":
    main()