def filtra_pares (a):
    '''int-> int'''
    b = ()
        if a[0]% 2 != 0:
            b = b + (a[0])
        if a[2]% 2 != 0:
            b = b + (a[2])
        if a[4]% 2 != 0:
            b = b + (a[4])
        if a[6]% 2 != 0:
            b = b + (a[6])
        return b