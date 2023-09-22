def faltante(lista):
    ma = max(lista)
    x = range(ma +1)
    if ma == len(lista):
        return ma + 1
    return sum(set(x) - set(lista))