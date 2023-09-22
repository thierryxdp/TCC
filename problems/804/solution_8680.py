def filtra_pares(tupla):
    """Retorna uma nova tupla contendo apenas elementos pares da tupla
    original na mesma ordem em que se encontravam
    tuple -> tuple"""
	lista = list(tupla)
    if lista[0] % 2 != 0:
        lista[0]= " "
    if lista[1] % 2 != 0:
        lista[1]= " "
    if lista[2] % 2 != 0:
        lista[2]= " "
    if lista[3] % 2 != 0:
        lista[3]= none 
	return tuple(lista)