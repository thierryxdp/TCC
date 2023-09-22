def fatorial(n):
    acum = n
    for i in list(range(1, n)):
        acum = acum * i
    return acum