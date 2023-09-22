def filtra_pares(tupla):
    '''função que recebe uma tupla com quatro elementos e retorna uma tupla com os elementos pares dessa tupla'''
    pares = []
    for item in tupla:
        if(item % 2 == 0):
            pares.append(item)
            
    return tuple(pares)