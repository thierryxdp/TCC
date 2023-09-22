def busca(setor: str, matriz: list) -> list:
    """comentário"""
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                del(matriz[i][j])
                dados.append(matriz[i])
        return dados