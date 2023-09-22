def filtra_pares(a,b,c,d):
    entrada = (a,b,c,d)
    filtra_pares = ()
    if (a % 2 == 0):
        filtra_pares = filtra_pares + entrada[0]
    if (b % 2 == 0):
    	filtra_pares = filtra_pares + entrada[1]
    if (c % 2 == 0):
    	filtra_pares = filtra_pares + entrada[2]
    if (d % 2 == 0):
        filtra_pares = filtra_pares + entrada[3]
    return filtra_pares