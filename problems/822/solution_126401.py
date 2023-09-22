def repetidos(lista):
    indice = 0
    contador = 0
    while indice<len(lista):
        if lista[indice] == lista[indice-1]:
            contador += 1
    return contador