def filtra_pares (tup):
    '''função que recebe uma tupla com quatro elementos
    inteiros como argumento e retorna uma nova tupla que
    contém apenas os elementos pares da tupla original, na
    ordem em que se encontravam'''
    if tup[0]%2: 
        return tup[0]
    elif tup[1]%2:
        return tup[1]
    elif tup[2]%2:
        return tup[2]
    elif tup[3]%2:
        return tup[3]