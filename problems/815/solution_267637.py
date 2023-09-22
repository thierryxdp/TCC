def insere(lista_numero,n):
	'''Função que recebe uma lista e um número inteiro n e retorna a lista em ordem crescente 
	incluindo o número recebido.
	Entrada: lista, int
	Saída: lista'''
	lista_numero.append(n)
	list.sort(lista_numero)
	return lista_numero