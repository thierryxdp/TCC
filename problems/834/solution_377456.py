def media_matriz(matriz):
    """
    Essa função calcula a média dos elementos de uma matriz
	Parametros: matriz (lista)
    Saida: float
    """
    soma=0
    for i in matriz:
        for c in i:
            soma = soma + c
    elementos = len(matriz[0])*len(matriz)
    media = soma/elementos
    return round(media,2)