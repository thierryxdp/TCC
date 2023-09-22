def faltante(lista):
    ''' '''
	listaCerta =[]
	listaSort = lista.sort()
	ultimoValor = len(lista)
	valor = lista[ultimoValor - 1]
	for z in range (1,valor + 1):
    	listaCerta.append(z)
	setLista = set(listaCerta) - set(lista)
	diferenca = set(setLista)
    return int(diferenca)