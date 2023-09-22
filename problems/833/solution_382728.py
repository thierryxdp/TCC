def conta_numero(numero, matriz):
    
    contador1 = 0
    contador2 = 0
    acumulador = 0
    
    m = len(matriz)
    n = len(matriz[0])
    
    while contador1 < m:
        while contador2 < n:
            if matriz[contador1][contador2] == numero:
                acumulador += 1
            contador2 += 1
        contador1 += 1
    
	return acumulador