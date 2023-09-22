# bolos
def bolos(A, B, C):
    """funcao que calcula e retorna a quantidade exata de bolos dado a quantidade da receita em relacao a quantidade que ele tem, int, int, int =>int"""
    return min((A//2), (B//3), (C//5))