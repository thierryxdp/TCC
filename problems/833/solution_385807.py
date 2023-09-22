def conta_numero(numero, matriz):
    '''
    	essa função recebe um número e uma matriz e retorna a quantidade de vezes que esse
        determinado número aparece na matriz dada.
        num, list -> num
    '''
	for i in matriz:
        if i == numero:
            return matriz.count(numero)
        else:
            return 0