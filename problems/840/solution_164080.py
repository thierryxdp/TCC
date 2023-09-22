def bolos(A,B,C):
    """Calcula e retorna o número exato de bolos que podem ser feitos de acordo com os igredientes disponíves"""
    return min(A//2,B//3,C//5)