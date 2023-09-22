#Start your python function here
def filtra_pares(a,b,c,d):
    '''Retorna uma nova tupla com elementos pares da tupla original. int, int, int, int -> int'''
    if a%2 == 0:
        return (a,)
    if b%2 == 0:
        return (,b,)
    if c%2 == 0:
        return (,c,)
    if d%2 == 0:
        return (,d,)
    else:
        return ()