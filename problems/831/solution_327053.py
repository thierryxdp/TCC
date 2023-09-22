'''Transforma uma palavra qualquer para a lingua do P'''
#str -> str
def lingua_p(palavra):
	lista = list(texto)
	novalista = []
	for i in range(0, len(lista)):
		if lista[i] in 'aeiouAEIOU':
			list.append(novalista, 'p' + lista[i] + 'p')
		else:
			list.append(novalista, lista[i])
	return str.join('', novalista)