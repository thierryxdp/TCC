def repetidos(lista):
    '''
    Função que recebe uma lista de números retorna quantas vezes um
    elemento da lista é igual ao seu anterior anterior
    list-> int
    '''
    pares = 0
    indice = 0
    while indice < (len(lista) - 1):
        if lista[indice] == lista[indice+1]:
            pares = pares + 1
        indice = indice + 1
    return pares