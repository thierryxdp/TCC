def faltante(lista):
    indice = 0
    lista = list.sort(lista)
    while indice < len(lista):
        if lista[indice] == indice + 1:
            indice = indice + 1
        else:
            return indice + 1