def media_matriz(matriz):
    """..."""
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    num_elementos = num_linhas * num_colunas
    soma = 0
    
    for i in range(num_linhas):
        for j in range(num_colunas):
            soma = soma + matriz[i][j]
    return round(soma/num_elementos,2)