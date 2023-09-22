def repetidos(lista):
    ''' '''
    indice=0
    soma= 0
    while indice < len(lista):
        if lista[indice] == lista[indice]-1:
        soma+=1
        indice+=1
    return soma