def repetidos(lista):
    '''Função retorna o numero de vezes que um elemento é igual ao elemento
    anterior;'''
    indice = 1
    element_seq = 0
    while indice < len(lista):
        if lista[indice-1] == lista[indice]:
            element_seq += 1
        indice += 1
    return element_seq