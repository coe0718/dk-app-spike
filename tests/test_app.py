import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import add, median, subtract  # noqa: E402


class App(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

    def test_median_odd_count(self):
        self.assertEqual(median([3, 1, 2]), 2)
        self.assertEqual(median([5]), 5)

    def test_median_even_count_is_float_mean_of_middle_two(self):
        result = median([4, 1, 3, 2])
        self.assertEqual(result, 2.5)
        self.assertIsInstance(result, float)
        result = median([1, 3])
        self.assertEqual(result, 2.0)
        self.assertIsInstance(result, float)

    def test_median_even_count_odd_sum_not_floored(self):
        # middle two sum to an odd number: integer division would give 1.0
        self.assertEqual(median([1, 2]), 1.5)
        self.assertEqual(median([1.0, 2.0]), 1.5)
        self.assertEqual(median([-2, -1]), -1.5)

    def test_median_reads_iterable_once(self):
        self.assertEqual(median(x for x in [9, 1, 5]), 5)
        self.assertEqual(median(iter([1, 2, 3, 4])), 2.5)

    def test_median_empty_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            median([])
        self.assertEqual(str(cm.exception), "median of no values")
        with self.assertRaises(ValueError):
            median(iter(()))

    def test_median_rejects_bool_and_non_numbers(self):
        for bad in ([1, True, 3], [True], ["a", 1], [1, None], [1, "2", 3], [1j, 2]):
            with self.subTest(bad=bad):
                with self.assertRaises(TypeError):
                    median(bad)


if __name__ == "__main__":
    unittest.main()
