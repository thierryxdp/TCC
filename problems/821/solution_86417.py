def fatorial(num):
    lista = list(range(num + 1))
    del lista[0]
    i = 0
    total = 1
    while (i < len(lista)):
        total = total * lista[i]
        i = i + 1
    return total