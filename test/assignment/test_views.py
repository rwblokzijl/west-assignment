from src.assignment.views import *

import unittest
import os

class TestViews(unittest.TestCase):

    """Test case docstring."""

    SLOW = bool(int(os.environ.get('SLOW', 0)))

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_call(self):
        return smallest_number_divisible(1, 5)

    def test_email_1(self):
        self.assertEqual(
                smallest_number_divisible(1, 10),
                2520
                )

    def test_email_2(self):
        self.assertEqual(
                smallest_number_divisible(1, 15),
                360360
                )

    def test_email_3(self):
        self.assertEqual(
                smallest_number_divisible(1, 25),
                26771144400
                )

    def test_negative_1(self):
        self.assertEqual(
                smallest_number_divisible(-1, 15),
                360360
                )

    def test_negative_1(self):
        self.assertEqual(
                smallest_number_divisible(-15, 15),
                360360
                )

    def test_negative_2(self):
        self.assertEqual(
                smallest_number_divisible(-15, -3),
                360360
                )

    def test_negative_3(self):
        self.assertEqual(
                smallest_number_divisible(-15, -15),
                15
                )

    def test_100(self):
        self.assertEqual(
                smallest_number_divisible(1, 100),
                69720375229712477164533808935312303556800
                )

    def test_1000(self):
        smallest_number_divisible(1, 1000)

    def test_10000(self):
        smallest_number_divisible(1, 10000)

    @unittest.skipUnless(SLOW, "Slow test") # takes about 1 second
    def test_100000(self):
        smallest_number_divisible(1, 100000)

    @unittest.skipUnless(SLOW, "Slow test") # takes about 20 seconds on my laptop
    def test_1000000(self):
        smallest_number_divisible(1, 1000000)

