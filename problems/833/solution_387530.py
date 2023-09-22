def conta_numero(numero,matriz):
    quantidade = 0
    numero = [numero]
    for i in range(0,len(matriz)):
        for j in range(0, len(matriz[0])):
        	if numero in matriz[i][j]:
            	quantidade +=1
    return quantidade