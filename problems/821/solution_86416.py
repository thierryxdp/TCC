def fatorial(num):
    lista = list(range(num + 1))
    del lista[0]
    i = 1
    total = 0
    while (i < len(lista)):
        total = total * (lista[i] * lista[i-1])
        i = i + 1
    return total