import unittest

from app import add, divide


class AddTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)


class DivideTest(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(1, 4), 0.25)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            divide(1, 0)
        self.assertNotIsInstance(cm.exception, ZeroDivisionError)
        self.assertIn("zero", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
