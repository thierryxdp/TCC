def repetidos(lista):
    '''função que dada uma lista de números, retorna o número de vezes que
    um elemento da lista é igual ao elemento anterior; list -> int'''
    i = 0
    vezes = 0
    while i < len(lista):
        if lista[i] == lista[i+1]:
            vezes = vezes + 1
        i = i + 1
    return vezes