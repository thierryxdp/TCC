def repetidos(lista):
    quantidade=0
    indice=1
    while indice<len(lista):
        if lista[indice]==lista[indice-1]:
            quantidade=quantidade+1
    return quantidade