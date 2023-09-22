def faltante(lista):
    return list(set(lista) - set(range(len(lista))))[0] + 1