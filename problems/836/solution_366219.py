def busca(setor,matriz):
    linha = 0
    coluna = 0
    posição = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                list.append(posição,matriz[i][j])
            	linha = linha + i
            	
            
                    
    return posição