import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import add, mean, subtract  # noqa: E402


class App(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

    def test_mean_basic(self):
        self.assertEqual(mean([1, 2, 6]), 3.0)
        self.assertEqual(mean([1.5, 2.5]), 2.0)

    def test_mean_generator_read_once(self):
        self.assertEqual(mean(x for x in [1, 2, 3]), 2.0)
        it = iter([1, 2, 3, 4])
        self.assertEqual(mean(it), 2.5)
        self.assertEqual(list(it), [])

    def test_mean_iterates_once(self):
        class Once:
            def __init__(self, items):
                self.items = items
                self.calls = 0

            def __iter__(self):
                self.calls += 1
                return iter(self.items)

        once = Once([1, 2, 3])
        self.assertEqual(mean(once), 2.0)
        self.assertEqual(once.calls, 1)

    def test_mean_empty(self):
        for empty in ([], (), iter(()), (x for x in [])):
            with self.assertRaises(ValueError) as cm:
                mean(empty)
            self.assertEqual(str(cm.exception), "mean of no values")

    def test_mean_rejects_bool(self):
        for bad in ([True], [1, 2, False], (b for b in [True, True])):
            with self.assertRaises(TypeError):
                mean(bad)

    def test_mean_rejects_non_numbers(self):
        for bad in (["1", 2], [None], [1, "x"], [1j], [[1]]):
            with self.assertRaises(TypeError):
                mean(bad)

    def test_mean_always_float(self):
        self.assertIs(type(mean([2, 2])), float)
        self.assertEqual(mean([2, 2]), 2.0)
        self.assertIs(type(mean([3])), float)


if __name__ == "__main__":
    unittest.main()
