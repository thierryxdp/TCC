def faltante(lista):
    ma = max(list)
    x = range(ma +1)
    if x == lista:
        return ma + 1
    return set(x) - set(lista)