def fatorial(n):
    cont = 1
    fatorial = [n]
    while cont< n:
        fat = n - cont
        fatorial += [fat]
        cont += 1
    return numpy.prod(fatorial)