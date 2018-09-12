from unittest import TestCase
from prime_number_table.prime_number_generator import PrimeNumberGenerator
from prime_number_table.exceptions import NotIntegerError, NotSupported


class PrimeNumberGeneratorTest(TestCase):
    def setUp(self):
        self.prime_number_table_multiplication = PrimeNumberGenerator()

    def test_class(self):
        self.assertIsInstance(self.prime_number_table_multiplication,
                              PrimeNumberGenerator)

    ''' This test checks the Exceptions '''
    def test_error_input(self):
        with self.assertRaises(NotIntegerError):
            self.prime_number_table_multiplication.create_list(primes="not int")
        with self.assertRaises(NotSupported):
            self.prime_number_table_multiplication.create_list(primes=-1)

    ''' This test evaluate the is_prime function'''
    def test_is_prime(self):
        self.assertTrue(self.prime_number_table_multiplication.is_prime(2))
        self.assertFalse(self.prime_number_table_multiplication.is_prime(4))
        self.assertFalse(self.prime_number_table_multiplication.is_prime(8))
        self.assertTrue(self.prime_number_table_multiplication.is_prime(13))
        self.assertFalse(self.prime_number_table_multiplication.is_prime(-4))

    ''' This test evaluate the usage of the feature flag '''
    def test_is_prime_with_optimization(self):
        # we toggle the optimization that does not work if we don't have the prime list yet
        self.prime_number_table_multiplication.toggle_feature_flag_optimize_prime_check()
        self.assertTrue(self.prime_number_table_multiplication.is_prime(9))
        # we fill the list
        self.prime_number_table_multiplication.create_list(primes=10)
        # Now we run the assertion again and the function works as expected
        self.assertFalse(self.prime_number_table_multiplication.is_prime(9))

    ''' This test checks if the prime list is correct '''
    def test_first_ten_primes(self):
        # we reset the test
        self.setUp()

        self.prime_number_table_multiplication.create_list(primes=0)
        self.assertEqual(self.prime_number_table_multiplication.prime_list, {})

        self.prime_number_table_multiplication.create_list(primes=10)
        first_primes = {2: True, 3: True, 5: True, 7: True, 11: True, 13: True,
                        17: True, 19: True, 23: True, 29: True}

        self.assertEqual(self.prime_number_table_multiplication.prime_list,
                         first_primes)
