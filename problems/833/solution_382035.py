def conta_numero(numero,matriz):
    vezes = 0
    linha = len(matriz)
    for x in range(1,linha+1):
    	if numero in matriz[x]:
        	vezes += 1
    return vezes