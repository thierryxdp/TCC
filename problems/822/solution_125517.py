def repetidos(lNumeros):
    '''Retorna o número de vezes que um elemento da lista de entrada é igual
       anterior;
       list -> int'''
    indice=1
    nRepetidos=0
    while indice<len(lNumeros):
        if lNumeros[indice]==lNumeros[indice-1]:
            nRepetidos+=1
        indice+=1
    return nRepetidos