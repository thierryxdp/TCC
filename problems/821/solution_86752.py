def fatorial(n):
    cont = 1
    fatorial = n*(n-1)
    while cont < n:
        fatorial = fatorial*cont
        cont = cont +1
    return fatorial