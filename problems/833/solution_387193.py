def conta_numero(numero,matriz):
    '''
    	A função recebe um numero inteiro e uma matriz contendo números inteiros e 
        retorna quantas vezes o número aparece na matriz.
        numero -> int
        matriz -> list (matriz de números inteiros)
        int, list -> int
    '''
    r = 0
    for i in matriz:
        for j in matriz[i]:
            if matriz[i][j] == numero:
                r += 1
	return r