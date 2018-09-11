from unittest import TestCase
from prime_number_table import Multiplication
from prime_number_table.exceptions import NotIntegerError, NotSupported


class AppTestCase(TestCase):

    def setUp(self):
        self.prime_number_table_multiplication = Multiplication()

    def testClass(self):
        self.assertIsInstance(self.prime_number_table_multiplication,
                              Multiplication)

    def testErrorInput(self):
        with self.assertRaises(NotIntegerError):
            self.prime_number_table_multiplication.createMatrix(primes="not int")
        with self.assertRaises(NotSupported):
            self.prime_number_table_multiplication.createMatrix(primes=-1)
