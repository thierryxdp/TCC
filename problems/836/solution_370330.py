def busca(busca: str, matriz: list) -> list:
    
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] in busca:
                list.remove(resultado[i], busca)
                resultado += [matriz[i],]
                
            
    return resultado