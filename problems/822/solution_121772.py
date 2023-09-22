def repetidos(lista_num):
    """Pede uma lista de números e reotrna
    o número de vezes em que um elemento da lista
    é igual ao elemento anterior.
    list->int"""
    repete = 0
    i = 1
    while i <len(lista_num):
        if lista_num[i]==lista_num[i-1]:
            repete = repete +1
        i = i + 1
    return repete