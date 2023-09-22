def conta_numero(numero, matriz):
    '''
    	Funcao que recebe um numero inteiro e uma matriz de
        inteiros de tamanho qualquer e retorna quantas vezes
        aquele numero aparece na matriz
        int, list -> int
    '''
    qtd = 0
    for i in matriz:
        for j in matriz:
        	if numero == matriz[j]:
            	qtd += 1
    return qtd