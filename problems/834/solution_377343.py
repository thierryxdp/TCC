def media_matriz(matriz):
    """função que dada uma matriz de inteiros não vazia, retorna a média de todos os numeros da matriz
    (com exatamente duas casa decimais de precisão)
    list -> float"""
  	soma == 0
    tamanho_matriz = 0

  	for linha in matriz:
    	soma += sum(linha)
    	tamanho_matriz += len(linha)

  	return round(soma / tamanho_matriz,2)