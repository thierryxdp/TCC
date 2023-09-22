def media_matriz(matriz):
    """função que dada uma matriz de inteiros não vazia, retorna a média de todos os numeros da matriz
    (com exatamente duas casa decimais de precisão)
    list -> float"""
    
    
  	somatorio = 0
  	tamanho_matriz = 0

  	for linha in matriz:
    	somatorio += sum(linha)
    	tamanho_matriz += len(linha)

  	return round(somatorio / tamanho_matriz,2)