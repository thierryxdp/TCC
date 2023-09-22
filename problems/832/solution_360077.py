def eh_quadrada(matriz: list) -> bool:
    """comentário"""
    for i in range(matriz):
        for j in range(matriz):
            if matriz[i] == matriz[j]:
                return True