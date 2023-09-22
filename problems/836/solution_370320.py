def busca(busca: str, matriz: list) -> list:
    
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    for i in range(linha):
        if list.index(matriz[i]) > 0:
            list.remove(matriz[i], busca)
    
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] in busca:
                resultado += [matriz[i],]
                
                
    return resultado