def busca(setor,matriz):
    linha = 0
    coluna = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
            	linha = linha + i
            	
            
                    
    return (linha,coluna)