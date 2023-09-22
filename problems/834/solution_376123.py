# Função media matriz

def media_matriz(matriz):
	'''Dada uma matriz de inteiros não vazia, retorna a nédia de todos os número da matriz com duas casas decimais de precĩsão.
	list(list) -> float'''
	soma = 0
	nlin = len(matriz)
	ncol = len(matriz[0])
	for linha in matriz:
		for aij in linha:
			soma += aij
	media = round(soma / (nlin * ncol) , 2)
	return media