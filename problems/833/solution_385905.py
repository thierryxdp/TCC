def conta_numero(numero,matriz):
    vezes=0
    for i in range(matriz):
    	if numero in matriz[i]:
                vezes+=1
    return vezes