def media_matriz(matriz):
    """
    Função para calcular a média, com duas casas décimais, de todos os termos de uma matriz.
    matriz - é a matriz que se deseja calcular a média dos termos.
    list(list) --> float
    """
    soma_termos = 0
    n_linha = len(matriz)
    n_coluna = len(matriz[0])
    for i in range(n_linha):
        for j in range(n_coluna):
            soma_termos += matriz[i][j]
    media = soma_termos / (n_linha * n_coluna)
    return round(media, 2)