def busca(busca: str, matriz: list) -> list:
    
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    i = 0
    
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] in busca:
                resultado += [matriz[i],]
                    
    
    if list.index(resultado[0], busca) == 1:
        list.remove(resultado[0], busca)
            
    return resultado