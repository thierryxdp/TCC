def repetidos(lista):
    contador=0
    indice=1
    while indice<len(lista):
        if lista[indice]==lista[indice-1]:
            contador=contador+1
        indice=indice+1
    return contador