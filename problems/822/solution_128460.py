def repetidos(listanumeros):
    '''Retorna o número de vezes em que um elemento da lista é igual ao anterior
    entrada: lista
    saída: int
    '''
    numerorepeticoes=0
    i=1
    while i<len(listanumeros):
        if listanumeros[i] == listanumeros[i-1]:
            numerorepeticoes=numerorepeticoes+1
        else:
            numerorepeticoes=numerorepeticoes
        i=i+1
    return numerorepeticoes