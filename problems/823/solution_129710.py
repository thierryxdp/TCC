def faltante(lista):
    x = 0
    if lista[0] != 1:
        return 1
    while x <= len(lista):
        if lista[x+1] != lista[x] + 1:
            return lista[x] + 1]
        x = x + 1