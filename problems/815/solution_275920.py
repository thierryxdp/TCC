def insere(lista_numero, n):
	"""A função recebe uma lista em ordem crescente e um valor inteiro 'n' e retorna a lista
	em ordem crescente com o valor 'n' adicionado
    list -> list"""
	x = lista_numero
	x.insert(-1, n)
	x.sort()
return x