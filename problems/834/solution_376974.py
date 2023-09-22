def media_matriz (matriz: list) -> float:
    """Retorna a média aritimética de todos os números em matriz, com preci
    são de duas casas decimais."""
    media = 0
    numero_de_linhas = len(matriz)
    numero_de_colunas = len(matriz[0])
    numero_de_elementos = numero_de_linhas * numero_de_colunas
    for linha_i in matriz:
        for coluna_j in linha_i:
            media += coluna_j
    return round(media/numero_de_elementos, 2)