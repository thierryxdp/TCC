def faltante(lista):
    indice = 0
    for el in lista:
        indice += 1
        print(el, indice)
        if el != indice:
            return el
    return len(lista) + 1