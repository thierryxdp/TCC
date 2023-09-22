def fatorial(n):
    cont = 1
    fatorial = [n]
    while cont< n:
        fat = (n - cont)
        n * fat = fatorial
        fatorial = fatorial * fat
        cont += 1
    return fatorial