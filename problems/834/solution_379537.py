def media_matriz(matriz):
    """dada uma matriz de inteiris não vazia, retorna a média de todos os números da matriz com duas casas decimais de precisão,
		(list) -> float"""
    soma = 0
    quantidade = 0
    for i in range(len(matriz)):
        quantidade = quantidade + len(matriz[i])
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
	return round(soma/quantidade,2)