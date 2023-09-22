def conta_numero(numero,matriz):
    if len(matriz) == 0:
        return 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
        	if numero in matriz[i][j]:
            	repete = list.count(matriz[i],numero)
    return repete