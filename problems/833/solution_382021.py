def conta_numero(numero,matriz):
	'''A função recebe um número inteiro uma matriz de inteiros calcula e retorna quantas ocorrências do número estão
    presentes na matriz.int,list->int'''
    qtd = 0
	for l in matriz:
		for n in l:
			if n == numero:
				qtd = qtd + 1
	return qtd