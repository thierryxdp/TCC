def conta_numero(numero,matriz):
    
    cont = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for linha in range(linhas):
        for coluna in range(colunas):
            
            if matriz[linha][coluna] == numero:
                cont += 1
                
	return cont