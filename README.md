# Prime Number Table
This project prints out the matrix of the first N prime number's multiplication. For instance the first 10 prime number's matrix looks like this:
```
2	3	5	7	11	13	17	19	23	29
3	9	15	21	33	39	51	57	69	87
5	15	25	35	55	65	85	95	115	145
7	21	35	49	77	91	119	133	161	203
11	33	55	77	121	143	187	209	253	319
13	39	65	91	143	169	221	247	299	377
17	51	85	119	187	221	289	323	391	493
19	57	95	133	209	247	323	361	437	551
23	69	115	161	253	299	391	437	529	667
29	87	145	203	319	377	493	551	667	841
```

## Requirements
You should have Docker installed on your system, with docker installed you should be abble to build the image and run it.

## Build Docker image
```
$make build
```

## Run program
The default way to run the command is with:
```
$make run
```
which runs for 10 primes, if you want to generate more primes simply use:
```
$make run PRIMES=20
```
Changing the default value for prime numbers to generate the matrix


## Run tests
```
$make test
```

## Remove old docker images
```
$make destroy
```

## Complexity analysis

Considering that we are running code on N primes, and we can consider some constant initialization `O(1)` (we are assuming that the maximum number fits on the size of the word of the computer, if not we need to consider Knuth's book, which is `O(WR)` where W+1 is number of machine words in the quotient and R is number of machine words in remainder for the modulo operand) our pseudo code is like this:

```
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
```

The complexy in time is `O(generate_primes) + O(Nˆ2)`.  `O(generate_primes)` is checking the number with all the primes that are less than its square root, similar to what the siege of Erastothenes does, `O(M log log M)` Where M is the maximum number generated. Which makes the complexity `O(M log log M)` considering that we cannot predict the maximum number generated. With the maximum number bigger than the memory word our complexity goes for `O(W R M log log M )`.

The complexity in space is `O(Nˆ2)` considering that we need to store the matrix of results.

It is possible to optimize the generation of the primes more using other sieges even more:
https://en.wikipedia.org/wiki/Generating_primes
