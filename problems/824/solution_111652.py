def uppCons(L):
    CT = 0
    F = ''
    while CT < len(L):
        if L[CT] in 'bcdfghjklmnpqrstvwxz':
            X = str.upper(L[CT])
            F = F + X
        elif L[CT] not in 'bcdfghjklmnpqrstvwxz':
            X = L[CT]
            F = F + X
            
        CT = CT + 1
	return F