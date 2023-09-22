def filtraMultiplos(lista,numero):
    """funcao"""
    listaF = []
    c = 0
    numerodetermosdalista = len(lista)
    while c < numerodetermosdalista:
        if (numero % lista[c]) == 0:
            listaF = listaF + [lista[c]]
            c = c + 1
    	else:
        	c = c + 1
	return listaF