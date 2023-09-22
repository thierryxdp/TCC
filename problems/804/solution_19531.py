def filtra_pares(tupla):
    '''Recebe uma tupla com quatro elementos e retorna uma nova tupla 
    contendo apenas os elementos pares
    tupla -> tupla'''
    nova = tupla[:]
    if nova % 2 == 0:
        return tupla