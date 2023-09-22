#Start your python function here
def filtra_pares(t):
    '''assinatura:
    tuple() -> tuple()
    '''
    u = ()
    if t[0] % 2 == 0:
        u = u + t[0]
    if t[1] % 2 == 0:
        u = u + t[1]
    if t[2] % 2 == 0:
        u = u + t[2]
    if t[3] % 2 == 0:
        u = u + t[3]
    return u