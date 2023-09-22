def fatorial(n):
    acum = 0
    for i in list(range(2, n)):
        acum += n * i
    return acum