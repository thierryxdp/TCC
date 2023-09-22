def conta_numero(numero, matriz):
    contador=0
	for i in range(len(matriz)):
        if numero in matriz[i]:
            contador+=matriz[i].count(numero)
    return contador