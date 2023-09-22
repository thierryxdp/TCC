def media_matriz(matriz):
	'''Função que dada uma matriz retorna a média de todos os
	números da mesma com duas casas decimais de precisão.
	Entrada: lista de listas
	Saída: float'''
	soma=0
	tamanho=0

	for linha in matriz:
		soma+=sum(linha)
		tamanho+=len(linha)
	return round(soma/tamanho,2)