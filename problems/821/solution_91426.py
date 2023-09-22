def fatorial(x):
    index = x
    resultado = 1
    while index > 0:
        resultado = resultado * index
        index = index - 1
    return resultado