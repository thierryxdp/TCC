def busca(busca: str, matriz: list) -> list:
    
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    a = 0
    
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] in busca:
                resultado += [matriz[i],]
    
    
    while len(resultado) > a:
        list.remove(resultado[a], busca)
        a = a + 1
   
    return resultado