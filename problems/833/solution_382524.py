def conta_numero(numero, matriz):
    '''recebe um int e uma matriz, retorna quantas vezes o int aparece
    na matriz'''
    qnt = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if numero in matriz[i][j]:
                qnt += 1
	return qnt