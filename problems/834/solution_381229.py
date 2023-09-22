def media_matriz(matriz):
    """retorna a media de todos os numeros da matriz"""
    i = 0
    while i >= len(matriz):
        i = i + matriz[i]
        i = i + 1
	return i/len(matriz)