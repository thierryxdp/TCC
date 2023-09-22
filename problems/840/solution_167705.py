def bolos (a,b,c):
    """Retorna a quantidade de bolos que podem ser feitos dado os ingredientes e a quantidade necessária"""
    return min(a//2,b//3,c//5)