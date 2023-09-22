def filtra_pares (e1,e2,e3,e4):
    '''c'''
    if (e1%2+e2%2+e3%2+e4%2)==0:
        return e1,e2,e3,e4
    if (e2%2+e3%2+e4%2)==0:
        return e2,e3,e4