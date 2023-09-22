def media_matriz(matriz):
    
    linhas = len(matriz)
    somador = 0
    
    for linha in range(linhas):
        colunas = len(matriz[0])
        divisor = linhas * colunas
        
        for coluna in range(colunas):
            
            somador += matriz[linha][coluna]
            
	media = somador / divisor
    
    return round(media,2)