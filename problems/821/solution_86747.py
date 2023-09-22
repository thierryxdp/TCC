def fatorial(n):
    cont = 1
    fatorial = n - cont
    while cont < n:
        fatorial = cont*fatorial 
        cont = cont +1
    return fatorial