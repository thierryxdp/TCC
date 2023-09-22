def fatorial(numero):
    i = 0
    f = 1
    while i in range(numero):
        f = f * (numero - i)
        i = i + 1
    return f