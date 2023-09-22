def bolos(A,B,C):
    """Retorna a quantidade maxima de bolo possivel de ser feita, dados os ingredientes"""
    return min(A//2,B//3,C//5)