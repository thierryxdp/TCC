def busca(setor: str, matriz: list) -> list:
    """comentário"""
    for i in range(len(matriz)):
        if matriz[i][0] == setor:
            return matriz[i]