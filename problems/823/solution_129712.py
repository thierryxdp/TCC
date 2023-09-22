def faltante(lista):
    x = 0
    if lista[0] != 1:
        return 1
    while x <= len(lista):
        if lista[x+1] != lista[x] + 1 and lista[x] != lista[-1]:
            return lista[x] + 1
        if lista[x] = lista[-1]:
            return lista[-1] + 1
        x = x + 1