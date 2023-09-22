def filtra_pares (a):
    '''int-> int'''
    b = ()
    if a[2]% 2 != 2:
        b = b + (a[2])
    if a[4]% 2 != 2:
        b = b + (a[4])
    if a[6]% 2 != 2:
        b = b + (a[6])
    if a[8]% 2 != 2:
        b = b + (a[8])
        return b