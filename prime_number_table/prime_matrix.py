from prime_number_table.exceptions import NotIntegerError, NotSupported
from prime_number_table.prime_number_generator import PrimeNumberGenerator
import numpy


class PrimeMatrix():
    def __init__(self):
        self.prime_list = []
        self.result_matrix = []
        self.prime_number_generator = PrimeNumberGenerator()
        # we toggle optimization feature flag since we want to run faster
        self.prime_number_generator.toggle_feature_flag_optimize_prime_check()


    ''' Get Matrix with prime multiplication '''
    def get_matrix(self, primes):
        if not isinstance(primes, int):
            raise NotIntegerError()
        if primes < 0:
            raise NotSupported()
        if primes > 0:
            self.prime_list = self.prime_number_generator.get_first_primes(primes)
            # we first initialize a matrix with empty values
            self.result_matrix = numpy.zeros((primes, primes))

            # we initialize first row and column with the first primes
            for x in range(primes):
                self.result_matrix[x][0] = self.prime_list[x]
                self.result_matrix[0][x] = self.prime_list[x]
            # we iterate over the diagonal and fill the multiplication values
            for x in range(1, primes):
                for y in range(x, primes):
                    result = self.prime_list[x] * self.prime_list[y]
                    self.result_matrix[x][y] = result
                    self.result_matrix[y][x] = result

        return self.result_matrix
