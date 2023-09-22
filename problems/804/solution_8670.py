def filtra_pares(tupla) tuple-> tuple:
    """Retorna uma nova tupla contendo apenas elementos pares da tupla
    original na mesma ordem em que se encontravam"""
   	lista= list(tupla)
    if lista[0] % 2 != 0:
        lista[0]= " "
    if lista[1] % 2 != 0:
        lista[1]= " "
    if lista[2] % 2 != 0:
        lista[2]= " "
    if lista[3] % 2 != 0:
        lsita[3]= " "
	return tuple(lista)