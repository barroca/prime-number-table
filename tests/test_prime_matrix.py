from unittest import TestCase
from prime_number_table.prime_matrix import PrimeMatrix
from prime_number_table.exceptions import NotIntegerError, NotSupported


class PrimeMatrixTest(TestCase):
    def setUp(self):
        self.prime_matrix = PrimeMatrix()

    def test_class(self):
        self.assertIsInstance(self.prime_matrix, PrimeMatrix)

    ''' This test checks the Exceptions '''
    def test_error_input(self):
        with self.assertRaises(NotIntegerError):
            self.prime_matrix.get_matrix(primes="not int")
        with self.assertRaises(NotSupported):
            self.prime_matrix.get_matrix(primes=-1)

    ''' Compare result of matrix '''
    def test_get_primes(self):
        self.assertTrue((self.prime_matrix.get_matrix(3) == [[2, 3, 5], [3, 9, 15], [5, 15, 25]]).all())
