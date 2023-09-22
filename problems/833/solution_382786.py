def conta_numero(numero, matriz):
    
    acumulador = 0
    
    if matriz != []:
        m = len(matriz)
        n = len(matriz[0])
        
    	for i in range(m):
        	for j in range(n):
            	if matriz[i][j] == numero:
                	acumulador += 1
    
    return acumulador