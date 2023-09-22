def par(n):
    if n%2==0:
        return True
    else:
        return False
    
def filtra_pares(t):
    '''recebe uma tupla com 4 elementos como parametro e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original;
    tup -> tup'''
    tuple(filter(par, t))