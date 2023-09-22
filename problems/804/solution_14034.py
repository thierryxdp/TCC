def filtra_pares(tuple):
    filtra_pares = tuple
    if (filtra_pares[0] % 2 == 0):
        filtra_pares = filtra_pares + filtra_pares[0]
    if (filtra_pares[1] % 2 == 0):
    	filtra_pares = filtra_pares + filtra_pares[1]
    if (filtra_pares[2] % 2 == 0):
    	filtra_pares = filtra_pares + filtra_pares[2]
    if (filtra_pares[3] % 2 == 0):
        filtra_pares = filtra_pares + filtra_pares[3]
    return filtra_pares