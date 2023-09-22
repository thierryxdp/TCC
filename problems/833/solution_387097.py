def conta_numero(numero, matriz):
    conta = 0
    n = -1
    i = 0
    while i < len(matriz):
        if numero in matriz:
            conta = conta + 1
            n = n + 1
        while i < len(matriz[n]):
           	if numero in matriz[n]:
                conta = conta + 1
            i = i + 1
	return conta