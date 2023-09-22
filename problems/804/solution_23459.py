def filtra_pares(a,b,c,d):
	x = [a,b,c,d]
    for y in x:
        if y%2==0:
            return tuple(x)