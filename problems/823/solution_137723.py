def faltante(lista):
    ''' '''
	listaCerta =[]
	listaSort = lista.sort()
	ultimoValor = len(lista)
	valor = lista[ultimoValor - 1]
	for z in range (1,valor + 1):
    	listaCerta.append(z)
	li_dif = [i for i in listaCerta + lista if i not in listaCerta or i not in lista] 
    return  li_dif[0]