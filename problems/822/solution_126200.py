def repetidos(lista):
    """ Insira uma lista e a funcao retornara o numero de vezes que um elemento da lista é
    igual ao elemento anterior"""
    n = 0
    r = 0
    while n+1 < len (lista):
        if lista [n] == lista [n+1]:
            r += 1
            num += 1
    return r