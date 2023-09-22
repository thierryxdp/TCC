def bolo (A,B,C):
    """Calcula a quantidade de bolo que podem ser produzidos, dados os ingredientes"""
    return max(A//2,B//3,C//5)