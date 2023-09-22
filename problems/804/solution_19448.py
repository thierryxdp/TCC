def par(n):
    '''função que retorna se um número n é par ou não'''
    # float -> bool
    return n % 2 == 0
def filtra_pares(tup):
    '''função que recebe uma tupla com quatro numeros e retorna uma nova tupla contendo os pares'''
    p = ()
    if par(tup[0]):
        p = p + (tup[0],)
    if par(tup[1]):
        p = p + (tup[1],)
    if par(tup[2]):
        p = p + (tup[2],)
    if par(tup[3]):
        p = p + (tup[3],)
    return p