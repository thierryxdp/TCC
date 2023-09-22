def repetidos(lista):
    '''Funcao que recebe uma lista numerica e retorna o numero de vezes que
    um elemento da lista e igual ao elemento anterior
    list -> int'''
    vezes = 0
    indice = 0
    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
            vezes = vezes + 1
        indice = indice + 1
    return vezes