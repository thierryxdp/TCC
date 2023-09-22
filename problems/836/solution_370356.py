def busca(busca: str, matriz: list) -> list:
    
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    i = 0
    
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] in busca:
                resultado += [matriz[i],]
                    
    while len(resultado) > i:
        list.remove(resultado[i], busca)
        i += 1
        
    return resultado