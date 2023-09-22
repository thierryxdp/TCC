#Start your python function here
def filtra_pares(a):
    '''a -> tupla de 4 elementos'''
    return sorted(filter( a[:] % 2 == 0, a))