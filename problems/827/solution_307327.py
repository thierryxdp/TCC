def qtd_divisores(n):
    """ Returns an unsorted list of the divisors of n """
    divs = [1]
    for p, e in factorization(n):
        divs += [x*p**k for k in range(1,e+1) for x in divs]
    return divs