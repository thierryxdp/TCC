def faltante(lista):
    indice = 0
    lista = list.sort(lista)
    if lista[indice] != indice + 1:
        return indice+1