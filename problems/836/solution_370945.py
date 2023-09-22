def busca(setor: str, matriz: list) -> list:
    """comentário"""
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            return matriz[i]
    else:
        return []