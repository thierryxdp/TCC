def filtra_pares (a):
    '''int-> int'''
    b = ()
    if a[2]% 2 != 0:
        b = b + (a[2])
    if a[8]% 2 != 0:
        b = b + (a[8])
    if a[10]% 2 != 0:
        b = b + (a[10])
    if a[12]% 2 != 0:
        b = b + (a[12])
        return b