def conta_numero(numero: int, matriz: list) -> int:
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    resultado = 0
    
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == numero:
                resultado += 1
                
    return resultado