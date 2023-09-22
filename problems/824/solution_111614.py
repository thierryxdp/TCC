def uppCons(L):
    CT = 0 
    F = ''
    while CT < len(L):
        if L[CT] in 'bcdfgjklmnpqrstvwxz':
            LT = str.upper(L[CT])
            F + LT
            
        else:
            F + L[CT]
    return F