def media_matriz(matriz:list)->float:
    """Calcula a média da matriz inserida
       
       Parameters:
       matriz: matriz de números inteiros não vazia
       
       Returns:
       média da matriz com duas casas decimais
    """
    nlin = len(matriz)
    ncol = len(matriz[0])
    soma = 0
    qtd_termos = nlin*ncol
    
    for i in range(nlin):
        for j in range(ncol):
            soma += matriz[i][j]
    return round(soma/qtd_termos,2)