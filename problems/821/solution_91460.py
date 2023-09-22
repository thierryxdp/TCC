def fatorial(x):
    n = 0
    valor = x
    while n < x:
        n += 1
        valor = valor*(x-n)
    return valor