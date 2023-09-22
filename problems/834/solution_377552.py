def media_matriz(m):
    soma = 0
    n = len(matriz)*lean(matriz[0])
    for i in list(range(len(m))):
    	for j in list(range(len(m[0]))):
            soma = soma + m[i][j]
    return soma/n