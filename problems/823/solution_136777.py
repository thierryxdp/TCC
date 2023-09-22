def faltante(lista):
    n = 0
    while n < len(lista):
        if lista[n+1] != lista[n] + 1:
            return lista[n] + 1
        else:
            return lista[n + 1]
        n = n + 1