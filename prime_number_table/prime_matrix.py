from prime_number_table.exceptions import NotIntegerError, NotSupported
from prime_number_table.prime_number_generator import PrimeNumberGenerator


class PrimeMatrix():
    def __init__(self):
        self.prime_list = []
        self.prime_number_generator = PrimeNumberGenerator()
        self.prime_number_generator.toggle_feature_flag_optimize_prime_check()


    ''' Get Matrix with prime multiplication '''
    def get_matrix(self, primes):
        if not isinstance(primes, int):
            raise NotIntegerError()
        if primes < 0:
            raise NotSupported()
        if primes > 0:
            self.prime_list = self.prime_number_generator.get_first_primes(primes)
        return self.prime_list
