def conta_numero(numero, matriz):
    '''
    	Funcao que recebe um numero inteiro e uma matriz de
        inteiros de tamanho qualquer e retorna quantas vezes
        aquele numero aparece na matriz
        int, list -> int
    '''
    linha = len(matriz)
    coluna = len(matriz[0])
    qtd = 0
    for i in linha:
        for j in coluna:
        	if numero == matriz[i][j]:
            	qtd += 1
    return qtd