'''Transforma uma palavra qualquer para a lingua do P'''
#str -> str
def lingua_p(palavra):
	lista = list(palavra)
	novalista = []
	for i in range(0, len(lista)):
		if lista[i] in 'aeiouAEIOU':
			list.append(novalista, lista[i] + 'p' + lista[i])
		else:
			list.append(novalista, lista[i])
	return str.join('', novalista)