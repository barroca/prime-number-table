from unittest import TestCase
from prime_number_table import Multiplication


class AppTestCase(TestCase):
    def testClass(self):
        prime_number_table_multiplication = Multiplication()
        self.assertIsInstance(prime_number_table_multiplication,
                              Multiplication)
