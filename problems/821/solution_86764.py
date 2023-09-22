def fatorial(n):
    cont = 1
    fatorial = [n]
    while cont< n:
        fat = (n - cont)
        fatorial = n * fat
        fatorial = fatorial * fat
        cont += 1
    return fatorial