def repetidos(lista):
    '''recebe uma lista e retorna o numero de vezes que um elemento da lista é igual ao anterior
    lista -> int'''
    indice = 0
    contador = 0
    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
            indice = indice + 1
            contador = contador + 1
        else:
            indice = indice + 1
    return contador