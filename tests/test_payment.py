
import unittest

from payment_services.payment import calculate_payment_total


class TestPaymentValidation(unittest.TestCase):

    def test_valid_payment(self):
        result = calculate_payment_total("49.99")

        self.assertEqual(result["amount"], 4999)
        self.assertEqual(result["currency"], "usd")
        self.assertEqual(result["status"], "pending")

    def test_zero_amount(self):
        with self.assertRaisesRegex(
            ValueError, "Payment amount must be positive"
        ):
            calculate_payment_total(0)

    def test_negative_amount(self):
        with self.assertRaisesRegex(
            ValueError, "Payment amount must be positive"
        ):
            calculate_payment_total(-10)

    def test_invalid_amount(self):
        with self.assertRaisesRegex(
            ValueError, "Invalid payment amount"
        ):
            calculate_payment_total("abc")

    def test_fractional_cents(self):
        with self.assertRaisesRegex(
            ValueError, "Amount cannot have fractional cents"
        ):
            calculate_payment_total("10.999")

    def test_unsupported_currency(self):
        with self.assertRaisesRegex(
            ValueError, "Only USD is supported"
        ):
            calculate_payment_total("10", "EUR")

    # Abdullah's second suggestion:
    # Lowercase currency must be accepted
    def test_lowercase_currency(self):
        result = calculate_payment_total("10", "usd")

        self.assertEqual(result["amount"], 1000)
        self.assertEqual(result["currency"], "usd")
        self.assertEqual(result["status"], "pending")


if __name__ == "__main__":
    unittest.main()
