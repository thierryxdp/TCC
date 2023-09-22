def filtra_pares(p):
    '''filtra os pares da tupla original'''
    pares=[]
    if p[0]%2==0:
        pares = pares + (0,p[0])
    if p[1]%2==0:
        pares = pares +  (1,p[1])
    if p[2]%2==0:
        pares = pares + (2,p[2])
    if p[3]%2==0:
        pares = pares + (3,p[3])
        return tuple(pares)