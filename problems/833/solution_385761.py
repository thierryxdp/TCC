def conta_numero(numero, matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros de
	tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz.
    int, list -> int'''
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                contador += 1
	return contador