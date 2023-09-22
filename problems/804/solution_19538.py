def filtra_pares(tupla):
    '''Recebe uma tupla com quatro elementos e retorna uma nova tupla 
    contendo apenas os elementos pares
    tupla -> tupla'''
    pares = tuple(tupla)
    if pares % 2 == 0:
        return pares