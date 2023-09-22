def fatorial(n):
    cont = 1
    fatorial = n*(n-cont)
    while cont < n:
        fatorial = fatorial*cont
        cont = cont +1
    return fatorial