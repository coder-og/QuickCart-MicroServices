
import unittest

from payment_services.payment import calculate_payment_total


class TestPaymentValidation(unittest.TestCase):

    def test_valid_payment(self):
        result = calculate_payment_total("49.99")
        self.assertEqual(result["amount"], 4999)
        self.assertEqual(result["currency"], "usd")
        self.assertEqual(result["status"], "pending")

    def test_zero_amount(self):
        with self.assertRaises(ValueError):
            calculate_payment_total(0)

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            calculate_payment_total(-10)

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            calculate_payment_total("abc")

    def test_fractional_cents(self):
        with self.assertRaises(ValueError):
            calculate_payment_total("10.999")

    def test_unsupported_currency(self):
        with self.assertRaises(ValueError):
            calculate_payment_total("10.00", "EUR")


if __name__ == "__main__":
    unittest.main()
