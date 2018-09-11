
class Multiplication():
    def __init__(self, primes=10):
        self.primes = primes
        self.prime_list = {2: True}

    def fillPrimes(self):
        primes_found = 0
        numberToCheck = 2
        while primes_found < self.primes:
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
            # we take the advantage of checking only on prime numbers
            if div in self.prime_list:
                if number % div == 0:
                    return False
            div += 1
        return True
