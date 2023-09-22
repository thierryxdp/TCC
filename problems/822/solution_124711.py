def repetidos(lista):
    repetidos = 0
    indice = 1 
    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
           repetidos = repetidos + 1
        indice = indice +1
    return repetidos