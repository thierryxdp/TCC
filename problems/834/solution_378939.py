def media_matriz(matriz):
    """Dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz;
    list -> double"""
    contador1 = 0
    media = 0
    while contador1 < len(matriz):
        contador2 = 0
        while contador2 < len(matriz[contador1]):
            lista = matriz[contador1]
            numero = lista[contador2]
            media += numero
            contador2 += 1
        contador1 += 1
    num = len(matriz) * len(matriz[0])
	media = media/num
    return round(media,2)