def repetidos(lista):
    """ Insira uma lista e a funcao retornara o numero de vezes que um elemento da lista é
    igual ao elemento anterior"""
    num = 0
    r = 0
    while num+1 < len(lista):
        if lista [num] == lista [num+1]:
            r += 1
    num += 1
    return r