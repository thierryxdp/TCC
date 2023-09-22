def maiores(listaNum, n):
	lista = []
	for i in range(len(listaNum)):
        if listaNum[i] > n:
            lista.append(listaNum[i])
    lista = sorted(lista)   
    return lista