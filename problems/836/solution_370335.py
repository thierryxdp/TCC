def busca(busca: str, matriz: list) -> list:
    
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] in busca:
                resultado += [matriz[i],]
    
    linhaR = len(resultado)
    colunaR = len(resultado[0])
    
    for a in range(linhaR):
        for b in range(colunaR)
        if list.index(resultado[a], busca) == 1:
            list.remove(resultado[a][b], busca)
        
            
    return resultado