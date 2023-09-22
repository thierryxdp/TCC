def filtra_pares(tupla):
    '''função que recebe uma tupla com quatro elementos
    e retorna uma tupla contendo os elementos pares desta'''
    pares = []
    for item in tupla:
        if(item % 2 == 0):
            pares.append(item)
    return tuple(pares)