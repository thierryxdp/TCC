def busca(setor: str, matriz: list) -> list:
    """comentário"""
    dados = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            del(matriz[i][2])
            dados.append(matriz[i])
    return dados
else:
        return []