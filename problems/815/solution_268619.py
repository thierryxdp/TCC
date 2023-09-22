def insere(lista_numero, n):
    """essa funcao, dada uma lista ordenada de numeros inteiros e um numero inteiro n,
	 insere n na posicao correta mantendo a lista ordenada"""
    lista_numero.insert(0, n)
    ordenada = sorted(lista_numero)
    return ordenada