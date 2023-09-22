def repetidos(lista_num):
    '''Esta função retorna o numero de vezes que um elemento da lista
    é igual ao elemento anterior.
    list >>> int '''
    contador = 1
    vezes = 0
    
	while len(lista_num) > contador:
		if lista_num[contador] == lista_num[contador - 1]:
			vezes += 1
			contador += 1
		else:
			contador += 1
	return vezes