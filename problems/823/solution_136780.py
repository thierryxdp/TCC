def faltante(lista):
    n = 0
    while n < len(lista) - 1:
        if lista[n+1] != lista[n] + 1:
            return lista[n] + 1
        n = n + 1
    return lista[n] + 1