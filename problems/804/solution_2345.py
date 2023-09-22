#Start your python function here
def filtra_pares(a):
    '''a -> tupla de 4 elementos'''
    return tuple filter(lambda x: x%2==0, a)