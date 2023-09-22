def bolos(A=2, B=3, C=5):
    """Retorna a quantidade de bolos que joão pode fazer com
    determinada quantidade de ingredientes.
    int, int -> int"""
    return min(A // 2, B // 3, C // 5)