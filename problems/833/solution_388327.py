def conta_numero(numero,matriz):
	"""Função que conta quantas vezes o número aparece
na matriz.
signature: integer, matrix --> integer """
    lin = 0
    col = 0
    qua = 0
    if len(matriz) > 0:
        for i in range(len(matriz)):
            for j in range(len(matriz[0]):
            	if numero == matriz[i][j]:
                	qua += 1
    return qua