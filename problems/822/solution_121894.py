def repetidos(lista):
    '''Função que recebe uma lista de números e retorne o número de vezes que um elemento da lista é igual ao elemento anterior; list->int'''
    contador=0
    vezes=0
    while lista[contador]<len(lista):
        if lista[contador]==lista[contador-1]:
            vezes=vezes+1
        else:
            vezes=vezes
    return vezes