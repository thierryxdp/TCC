def repetidos(lista):
    '''função que dada uma lista de números retorna o
    número de vezes que um elemento da lista é igual ao
    anterior
    list -> int
    '''
    quantidade = 0
    indice = 0
    while indice >= 0 and indice < len(lista)-1:
        if lista[indice+1] == lista[indice]:
            quantidade += 1
        indice += 1
    return quantidade