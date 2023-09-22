def conta_numero(numero, matriz):
    l1 = len(matriz)
    if matriz == []:
        return 0
    else:
    	l2 = len(matriz[0])
    count = 0
    for i in range(l1):
        for j in range(l2):
            if matriz[i][j] == numero:
            	count += 1
   	
    return count