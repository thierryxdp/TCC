def conta_numero(numero,matriz):
    '''função que calcula e retorna quantas vezes um numero
    aparece na matriz
    parametros:
    int,list->int'''
    m = matriz [:]
    conta = 0
	for lista in matriz:
		for elem in lista:
            if elem == numero:
				conta+=0
	return conta