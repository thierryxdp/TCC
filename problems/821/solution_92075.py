def fatorial(n):
    acum = 0
    for i in list(range(1, n)):
        acum += n * i
    return acum