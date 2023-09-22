def filtraMultiplos(lista,n):
    """lista -> lista"""
    contador = 0
    juntar = []
    while contador < len(lista):
        if  n % lista[contador] == 0:
            juntar = juntar + [lista[contador]]
            contador += 1
	    else:
            pass
	return juntar