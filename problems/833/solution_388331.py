def conta_numero(numero,matriz):
	"""Função que conta quantas vezes o número aparece
na matriz.
signature: integer, matrix --> integer """
	qua = 0
    if len(matriz) > 0:
    	for i in range(len(matriz)):
        	for y in range(len(matriz[0]):
            	if numero == matriz[i][y]:
                	qua += 1
    return qua