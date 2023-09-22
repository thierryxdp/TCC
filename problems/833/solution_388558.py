def conta_numero(num, matriz):
    '''função que dado um número inteiro e uma matriz
    de inteiros de tamanho qualquer, conta e retorna quantas
    vezes aquele número aparece na matriz; 
     int,int -> int'''
    i = 0
    for linha in matriz:
        i += list.count(linha, num)
	return i