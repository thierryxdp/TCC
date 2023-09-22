def filtra_pares(a,b,c,d):
    '''
    '''
	if a%2 == 0:
        par = a
    elif b%2 == 0:
        sim = b
    elif c%2 == 0:
        med = c
    elif d%2 == 0:
        fal = d
        return 'par' + 'sim' + 'med'+ 'fal'