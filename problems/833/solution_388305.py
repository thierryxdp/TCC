def conta_numero(numero, matriz):
    '''Função que, dado um inteiro e uma matriz de inteiros
    de qualquer dimensão, conta e retorna quantas vezes o
    dado número aparece na matriz
    int, list -> int'''
    cont = 0
    for item in matriz:
        for j in range(len(item)):
        	if item[j] == numero:
            	cont += 1
    return cont