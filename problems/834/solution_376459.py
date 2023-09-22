def media_matriz(matriz):
    '''retorna a media de todos os numeros da matriz, com duas casas decimais'''
    soma = 0
    divisor = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            soma += matriz[i][j]
            divisor += 1
	media = soma/divisor
    return media