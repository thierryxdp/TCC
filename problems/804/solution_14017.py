def filtra_pares(a):
    entrada = (a,)
    filtra_pares = ()
    if (entrada[0] % 2 == 0):
        filtra_pares = filtra_pares + entrada[0]
    if (entrada[1] % 2 == 0):
    	filtra_pares = filtra_pares + entrada[1]
    if (entrada[2] % 2 == 0):
    	filtra_pares = filtra_pares + entrada[2]
    if (entrada[3] % 2 == 0):
        filtra_pares = filtra_pares + entrada[3]
    return filtra_pares