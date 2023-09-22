def bolos(A,B,C):
    """calcula a quantidade de bolos que podem ser feitos dado o número de ingredientes necessários para um bolo e a quantidade disponivel"""
    return min(A//2,B//3,C//5)