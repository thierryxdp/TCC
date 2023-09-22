def filtra_pares(t()): 

    pares = ''
	
    if t[0] % 2 == 0:
        pares += str(t[0])

    elif t[1] % 2 == 0:
        pares += str(t[1])

    elif t[2] % 2 == 0:
        pares += str(t[2])

    elif t[3] % 2 == 0:
        pares += str(t[3])

    elemPares = pares
    return elemPares