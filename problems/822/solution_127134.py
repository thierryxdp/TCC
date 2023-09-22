def repetidos(listaNum):
	''' função que conta quantas vezes o elemento se repetiu
	list --> int'''
	ctd = 1
	vezes = 0
	while len(listaNum) > ctd:
		if listaNum[ctd] == listaNum[ctd -1]:
			vezes += 1
			ctd += 1
		else:
			ctd += 1
	return vezes