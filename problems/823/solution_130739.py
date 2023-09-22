def faltante (lista):
    indice = 1
    lista.sort()
    while lista [ indice - 1] == indice:
        indice += 1 
        if indice > len(lista):
            return indice 
    return indice