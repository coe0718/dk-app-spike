import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import add, divide, subtract  # noqa: E402


class App(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)


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
