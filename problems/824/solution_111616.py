def uppCons(L):
    CT = 0 
    F = ''
    while CT < len(L):
        if L[CT] in 'bcdfgjklmnpqrstvwxz':
            LT = str.upper(L[CT])
            F + LT
            CT + 1
        else:
            F + L[CT]
            CT + 1
    return F