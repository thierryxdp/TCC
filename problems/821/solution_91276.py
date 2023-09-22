def fatorial(numero):
    i = 0
    fat = 1
    n = numero
    while i < numero:
        fatorial = fatorial * n
        n = n - 1
        i = i + 1
    return fatorial