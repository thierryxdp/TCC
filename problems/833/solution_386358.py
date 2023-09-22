def conta_numero(numero,matriz):
    '''Dado um número inteiro e uma matriz de inteiros,
    retorna quantas vezes o número aparece na matriz;
    str,list(list[str]) -> str'''
    contador=0
    linhas=len(matriz)
    colunas=len(matriz[0])
 	for i in range(linhas):
 		for j in range(colunas):
 			if matriz[i][j]==numero:
 				contador+=contador
 	return contador