# Prime Number Table
This project prints out the matrix of the first N prime number's multiplication. 

## Requirements
You should have Docker installed on your system, with docker installed you should be abble to build the image and run it. 

## Build Docker image
$make build

## Run program
$make run

## Run tests
$make test

## Remove old docker images
$make destroy

## Complexity analysis

Considering that we are running code on N primes, and we can consider some constant initialization O(1) our pseudo code is like this:


matrix:
    generate_primes(N)
    initialize_matrix(N)
    for x from 0->N-1:
        initialize_matrix[x][0]
        initialize_matrix[0][x]
    for x from 0->N-1:
        for y from x->N-1:
            initialize_matrix[x][y]
            initialize_matrix[y][x]


the complexy is O(generate_primes) + O(Nˆ2).  O(generate_primes) is checking the number with all the primes that are less than its square root, similar to what the siege of Erastothenes do, O(Mlog log M) Where M is the maximum number generated

