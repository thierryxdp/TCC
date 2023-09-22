#Start your python function here
def filtra_pares(t):
    ''' Retorna uma tupla com apenas números inteiros pares,
    a partir da dada tupla
    tuple -> tuple'''
    a,b,c,d = t

    new_tuple = ()
    if a % 2 == 0:
        new_tuple = new_tuple + (a,)

    if b % 2 == 0:
        new_tuple = new_tuple + (b,)

    if c % 2 == 0:
        new_tuple = new_tuple + (c,)

    if d % 2 == 0:
        new_tuple = new_tuple + (d,)

    return new_tuple