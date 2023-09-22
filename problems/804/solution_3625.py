def filtra_pares(tupla(a,b,c,d)):

    lista = []

    for valor in tupla(a,b,c,d):
    	if valor % 2 == 0:
        	lista.append(valor)

	return (lista)