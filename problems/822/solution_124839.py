def repetidos(lista_num):
    '''Recebe uma lista de números e retorna o número
    de vezes em que um elemento da lista é igual ao
    seu antecessor
    list -> int'''
    rep = 0
    i = 1
    while i < len(lista_num):
        if lista_num[i] == lista_num[i-1]:
            lista_rep += 1
        i += 1
    return rep