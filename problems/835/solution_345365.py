def melhor_volta(matriz):
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    lista = []
    
    for linha in range(linhas):
        for coluna in range(colunas):
            
            list.append(lista,matriz[linha][coluna])
            
	tempo = min(lista)
    
    for linha in range(linhas):
        for coluna in range(colunas):
            
            if matriz[linha][coluna] == tempo:
                corredor = linha + 1
                volta = coluna + 1
                
	return corredor, tempo, volta