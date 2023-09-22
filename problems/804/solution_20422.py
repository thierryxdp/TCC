def filtra_pares(p):
    '''filtra os pares da tupla original'''
    pares=[]
    if p[0]%2==0:
        pares.insert(0,a[0])
    if p[1]%2==0:
        pares.insert(1,a[1])
    if p[2]%2==0:
        pares.insert(2,a[2])
    if p[3]%2==0:
        pares.insert(3,a[3])
        return tuple(pares)