from unittest import TestCase
from prime_number_table.prime_matrix import PrimeMatrix
from prime_number_table.exceptions import NotIntegerError, NotSupported


class PrimeMatrixTest(TestCase):
    def setUp(self):
        self.prime_matrix = PrimeMatrix()

    def test_class(self):
        self.assertIsInstance(self.prime_matrix, PrimeMatrix)

    def test_get_primes(self):
        self.assertEqual(self.prime_matrix.get_matrix(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
