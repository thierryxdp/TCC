def bolos(A, B, C):
    """retorna a quantidade de bolos inteiros que da para fazer com a quantidade
    (A) de farinha de trigo, (B) de ovos e (C) colheres de sopa de leite"""
    return min(A//2, B//3, C//5)