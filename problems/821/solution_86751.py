def fatorial(n):
    cont = 1
    fatorial = n - cont
    while cont < n:
        fatorial = (n-1) *fatorial
        cont = cont +1
    return fatorial