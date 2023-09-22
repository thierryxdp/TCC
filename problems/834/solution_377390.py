def media_matriz(matriz):
    """função que dada uma matriz de inteiros não vazia, retorna a média de todos os numeros da matriz
    (com exatamente duas casa decimais de precisão)
    list -> float"""
    nlin = len(matriz)
    ncolun = len(matriz[0])
    
    import numpy
	x = numpy.array(matriz)
    y=numpy.prod(x)
    media = 0
  for i in range(len(matriz)):
        	for j in range(len(matriz[i])):
            	media += valor [i][j]
            
    return round(2,media)