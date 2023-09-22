def par(z):
    if z%2==0:
        return True
    else:
        return False

def filtra_pares(z):
    '''Recebe uma tupla com 4 elementos e retorna uma nova tupla com apenas os elementos pares'''
    return list(filter(par,z))