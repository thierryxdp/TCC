def filtra_pares(tupla):
    '''função que recebe tupla com quatro elementos e retorna uma tupla contendo os elementos pares dela'''
    pares = []
    for item in tupla:
        if(item % 2==0):
            pares.append(item)
    return tuple(pares)