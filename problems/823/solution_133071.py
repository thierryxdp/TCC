def faltante(lista):
    '''Função que, dada uma lista numérica, devolve o valor
    que a complementa de modo a manter a ordem crescente'''
	lista.sort()
	lista2 = list(range(1,lista[-1]))
	i = 0
	if lista[0] != 1:
		return 1
	else:
		try:
			while lista[i] == lista2[i]:
				i += 1
			return lista2[i]
		except:
			return lista[-1]+1