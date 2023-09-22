def filtra_pares (e1,e2,e3,e4):
    '''c'''
    t=()
    if e1%2 ==0:
        return t+(e1,)
    if e2%2 ==0:
        return t+(e1,e2,)
    if e3%2 ==0:
        return t+(e1,e2,e3,)
    if e4%2 ==0:
        return t+(e1,e2,e3,e4,)