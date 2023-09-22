def conta_numero(numero, matriz):
    """ Função que dado um número inteiro e uma matriz de inteiros de qualquer tamanho, conta e retorna quantas vezes aquele número aparece na matriz
    	list-> int
    """
    contador = 0
    
	for lista in matriz:
		for elem in lista:
			if elem == numero:
				contador +=1
	return contador