def media_matriz(matriz):
    """
    lista-> float
    :param matriz: Recebe uma matriz de inteiros
    :param return: Retorna a medias desses nuemros em duas casas decimais
    """
    quantidade_linhas = len(matriz)
    quantidade_coluna = len(matriz[0])
    soma_elementos = 0
    for linha_matriz in range(quantidade_linhas):
        soma_elementos = 0
        for elementos_linha in range(quantidade_colunas):
            soma_dos_elementos += matriz[linha_matriz][elementos_linha]
        soma_elementos_matriz += soma_elementos_linha
   	quantidade_elementos_matriz = quantidade_linhas * quantidade_coluna
    media_matriz = soma_elementos_matriz/quantidade_elementos_matriz
    return round (media_matriz,2)