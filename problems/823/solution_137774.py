def faltante(lista):
    return list(set(lista) - set(range(len(lista) - 1)))[0] + 1