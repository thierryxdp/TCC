def faltante(lista):
    i = 1
    while i < len(lista):
        n = lista[i]
        if n - 1 != lista[i - 1]:
            r = r + (lista[i] - 1)
            i = i + 1
        i = i + 1
    return r