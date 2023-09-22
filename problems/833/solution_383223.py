def conta_numero(num,matriz):
    """..."""
    
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    contador = 0
    
    for i in range(num_linhas):
        for j in range(num_colunas):
            if matriz[i][j] == num:
                contador = contador + 1
    return contador