
from decimal import Decimal, InvalidOperation


def calculate_payment_total(amount, currency="USD"):
    """Validate and prepare a payment amount."""

    try:
        amount = Decimal(str(amount))
    except (InvalidOperation, ValueError):
        raise ValueError("Invalid payment amount")

    if not amount.is_finite() or amount <= 0:
        raise ValueError("Payment amount must be positive")

    if currency != "USD":
        raise ValueError("Only USD is supported")

    amount_cents = amount * 100

    if amount_cents != amount_cents.to_integral_value():
        raise ValueError("Amount cannot have fractional cents")

    return {
        "amount": int(amount_cents),
        "currency": currency.lower(),
        "status": "pending",
    }


if __name__ == "__main__":
    payment = calculate_payment_total("49.99")
    print("Payment prepared:", payment)
