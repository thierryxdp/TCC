def repetidos(lista:list) -> int:
    '''Retorna a quantidade de vezes que um elemento da lista
    é igual ao elemento anterior'''
    return filter(lambda x: x == x-1, lista)