def filtra_pares (a):
    '''int-> int'''
    b = ()
    if a[2]% 2 != 0:
        b = b + (a[2])
    if a[6]% 2 != 0:
        b = b + (a[6])
    if a[10]% 2 != 0:
        b = b + (a[10])
    if a[12]% 2 != 0:
        b = b + (a[12])
        return b