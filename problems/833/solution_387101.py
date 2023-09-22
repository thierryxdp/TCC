def conta_numero(numero, matriz):
    conta = 0
    for i in range(len(matriz)):
        for h in range(len(matriz[i])):
        	if numero == matriz[i][h]:
            	conta = conta + 1
    return conta