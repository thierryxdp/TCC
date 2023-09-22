def faltante(lista):
    for elem in lista:
        if elem in range(lista[0:]):
            return elem