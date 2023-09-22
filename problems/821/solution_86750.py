def fatorial(n):
    cont = 1
    fatorial = n - cont
    while cont < n:
        fatorial = n*(n-1)
        cont = cont +1
    return fatorial