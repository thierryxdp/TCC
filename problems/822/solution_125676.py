def repetidos(lista):
    '''funcao que retorna a quatidade de vezes
    que um numero é repetido em uma lista
    entrada: lista
    saida: inetiro
    '''
    indice= 1 
    vezes= 0
    while indice<len(lista):
        if lista[(indice-1)]==lista[indice]:
            vezes= vezes + 1
        indice= indice + 1
    return vezes