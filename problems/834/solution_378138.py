def media_matriz(matriz):
    """Retorna a a media de todos os números da matriz 
    inserida(com duas casas decimais de precisão);
    list -> float"""
    n_colunas = len(matriz[0])
    n_linhas = len(matriz)
    n_elementos= n_colunas * n_linhas
    acumulador = 0
    for i in range(n_linhas):
        for j in range(n_colunas):
            acumulador = acumulador + a[i][j]
            
    media = round(acumulador/ n_elementos, 2)
    return media