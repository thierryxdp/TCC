def busca(busca: str, matriz: list) -> list:
    
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] in busca:
                resultado += [matriz[i],]
    
    linhaR = len(resultado)        
    for a in range(linhaR):
        if list.index(resultado[a], busca) == 1:
            list.remove(resultado[a], busca)
        
            
    return resultado