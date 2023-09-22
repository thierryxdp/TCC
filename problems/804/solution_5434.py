def filtra_pares(a,b,c,d):
    '''Função que retorna uma nova tupla contendo apenas
    os elemetos pares da tupla original, na mesma ordem em que
    se encontravam.
    a=int,b=int,c=int,d=int->tuple'''
    return tuple(filtra_pares((a,b,c,d)//2))