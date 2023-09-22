def filtra_pares(a,b,c,d):
    filtra_pares = ()
    if a % 2 == 0:
        filtra_pares = filtra_pares + (a,)
    if b % 2 == 0:
    	filtra_pares = filtra_pares + (b,)
    if c % 2 == 0:
    	filtra_pares = filtra_pares + (c,)
    if d % 2 == 0:
        filtra_pares = filtra_pares + (d,)
	return filtra_pares