def conta_numero(numero,matriz):
    quantidade = 0
    for i in range(0,len(matriz)):
        for j in range (0, len(matriz[0])):
        	if numero in matriz[i]:
            	quantidade +=1
    return quantidade