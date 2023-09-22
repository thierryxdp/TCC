def conta_numero(n, matriz):
    '''função que dado um número inteiro e uma matriz
    de inteiros de tamanho qualquer, conta e retorna quantas
    vezes aquele número aparece na matriz; 
     int,int -> int'''
    x = 0
    for linha in matriz:
        x = x + list.count(linha, n)
	return x