def eh_quadrada(matriz: list) -> bool:
    """comentário"""
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i] == matriz[j]:
                return True