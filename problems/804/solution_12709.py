def filtra_pares (a):
    '''tuple -> tuple'''
    b = []
    
    if a[0]% 2 == 0:
        b = b + (a[0],)
    return b