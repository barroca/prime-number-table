#!/usr/bin/python3
import argparse
from prime_number_table.prime_matrix import PrimeMatrix


def main(args):
    prime_matrix = PrimeMatrix()
    matrix = prime_matrix.get_matrix(primes)
    # use pythonic way to print data organized
    print('\n'.join(['\t'.join([str(int(cell)) for cell in row]) for row in matrix]))


if __name__ == "__main__":
    # parse args for number of primes to run
    parser = argparse.ArgumentParser()
    parser.add_argument("primes", type=int, help="Number of primes to generate matrix")
    args = parser.parse_args()
    primes = args.primes
    main(args)
