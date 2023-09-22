def faltante(lista):
    indice = 0
    for el in lista:
        indice += 1
        if el != indice:
            return indice
    return len(lista) + 1