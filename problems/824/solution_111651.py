def uppCons(L):
    CT = 0
    F = ''
    while CT < len(L):
        if L[CT] in 'bcdfgjklmnpqrstvwxz':
            X = str.upper(L[CT])
            F = F + X
        elif L[CT] not in 'bcdfgjklmnpqrstvwxz':
            X = L[CT]
            F = F + X
            
        CT = CT + 1
	return F