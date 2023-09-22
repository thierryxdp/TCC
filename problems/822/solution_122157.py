def repetidos(lista):
    '''Recebe como entrada uma lista de números, e retorna o número de vezes que um elemento da lista é igual ao elemento anterior
    list -> int'''
    i = 1
    j = 0
    qnts_elementos = 0
    while j < len(lista)-1:
        if lista[i] == lista[j]:
            i = i + 1
            j = j + 1
            qnts_elementos = qnts_elementos + 1
        else:
            i = i + 1
            j = j + 1
    return qnts_elementos