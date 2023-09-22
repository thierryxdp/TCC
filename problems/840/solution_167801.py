def bolos(A, B, C):
    """Função que retorna a quantidade máxima de bolos que poderão ser feitos"""
    return int(min(A/2,B/3, C/5))