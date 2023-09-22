def media_matriz(matriz):
    """Função que dada uma matriz de inteiros nao vazia, retorna a media de todos
    os numeros da matriz.
    list -> float"""
    soma = 0
    for i in matriz:
        for j in i:
            soma += j
	qtd = len(matriz)*len(matriz[0])
    return round(soma/qtd, 2)