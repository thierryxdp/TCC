def busca(busca: str, matriz: list) -> list:
    
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    i = 0
    
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] in busca:
                resultado += [matriz[i],]
                    
    for a in range(linha):
        if list.index(resultado[a], busca]) in busca:
            list.remove(resultado[a], busca)
        
    return resultado