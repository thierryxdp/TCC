def repetidos(lista):
    '''---'''
    indice = 1
    repetidos=[]
    while indice < len(lista):
        if lista[indice]==lista[indice-1]:
            repetidos.append(lista[indice])
        indice += 1
    return len(repetidos)