def conta_numero(num, matrix):
    '''Função que calcula o numero de vezes que um numero aparece em uma matriz
    Recebe um numero e uma matriz
    Retorna o numero de vezes que esse numero aparece'''
	contador = 0
	for lista in matrix:
		for elem in lista:
			if elem == num:
			    contador +=1
	return contador