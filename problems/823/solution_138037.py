def faltante(lista):
    i = 0
    falta = len(lista) + 1
    n = 1
    while i <= falta:
        if n != lista[n]:
            return n
        i = i + 1
        n = n + 1
    return falta