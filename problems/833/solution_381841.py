def conta_numero(numero,matriz):
    
    cont = 0
    linhas = len(matriz)
    
    
    for linha in range(linhas):
        
        colunas = len(matriz[0])
        for coluna in range(colunas):
            
            if matriz[linha][coluna] == numero:
                cont += 1
                
	return cont