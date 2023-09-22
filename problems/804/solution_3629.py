def filtra_pares([a,b,c,d]):

    lista = []

    for valor in [a,b,c,d]:
    	if valor % 2 == 0:
        	lista.append(valor)

	return (lista)