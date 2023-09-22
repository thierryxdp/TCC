def filtra_pares(tupla):
    '''Recebe uma tupla com quatro elementos e retorna uma nova tupla 
    contendo apenas os elementos pares
    tupla -> tupla'''
    pares = []
    for i in tupla:
        if i % 2 == 0:
            pares += [i]
    return tuple(pares)