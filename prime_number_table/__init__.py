from prime_number_table.exceptions import NotIntegerError, NotSupported


class Multiplication():
    def __init__(self):
        self.prime_list = {}
        self.prime_matrix = []
        self.feature_flag_optimize_prime_check = False

    ''' This function changes the feature flag that optimizes check by
        serching in the primes already found, the optimization only works
        for searches made in order '''
    def toggle_feature_flag_optimize_prime_check():
        self.feature_flag_optimize_prime_check =\
            not self.feature_flag_optimize_prime_check

    ''' Create Matrix containing all primes '''
    def createMatrix(self, primes=10):
        if not isinstance(primes, int):
            raise NotIntegerError()
        if primes < 0:
            raise NotSupported()
        self.fillPrimes(primes)

    ''' fill hash of prime numbers with the first primes_to_find '''
    def fillPrimes(self, primes_to_find=1):
        self.prime_list = {2: True}
        primes_found = 1
        numberToCheck = 2
        while primes_found < primes_to_find:
            if self.is_prime(numberToCheck):
                self.prime_list[numberToCheck] = True
                primes_found += 1
            numberToCheck += 1

    ''' Check if a number is prime'''
    def is_prime(self, number):
        # if a number is 2 or either divisble by 2 it is not prime
        if number < 2 or number % 2 == 0:
            return False
        # we iterate over other numbers from 3 until the square root of that
        # number and check it
        div = 3
        while div*div <= number:
            # check if feature flag is available
            if self.feature_flag_optimize_prime_check:
                # we take the advantage of checking only on prime numbers
                if div in self.prime_list:
                    if number % div == 0:
                        return False
            else:
                if number % div == 0:
                    return False
            div += 1
        return True
