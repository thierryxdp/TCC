def filtra_pares(tupla):
    """Retorna uma nova tupla contendo apenas elementos pares da tupla
    original na mesma ordem em que se encontravam
    tuple -> tuple"""
	if tupla[0] and tupla[1] and tupla[2] and tupla[3] % 2 == 0:
    	return list(tupla)
    elif tupla[0] and tupla[1] and tupla[2] % 2 == 0:
        return list(tupla[0:3])
    elif tupla[0] and tupla[3] % 2 == 0:
        return (list(tupla[0]) + list(tupla[3]))
    elif tupla[0] and tupla[1] % 2  == 0:
        return list(tupla[0:2])
	elif tupla[0] % 2 == 0:
        return list(tupla[0])