def faltante(lista):
    return list(set(lista) - set(range(1, len(lista))))[0]