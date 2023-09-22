def repetidos(lista):
    '''Recebe como entrada uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior
    list -> int'''
    i = 1
    qnts_elementos = 0
    while i-1 < len(lista):
        if lista[i] == lista[i-1]:
            qnts_elementos = qnts_elementos + 1
        i = i + 1
    return qnts_elementos