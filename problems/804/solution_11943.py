def filtra_pares (a):
    '''int-> int'''
    b = ()
    if a[6]% 2 != 2:
        b = b + (a[6])
    if a[8]% 2 != 2:
        b = b + (a[8])
    if a[10]% 2 != 2:
        b = b + (a[10])
    if a[12]% 2 != 2:
        b = b + (a[12])
        return b