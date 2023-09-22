def bolos(A,B,C):
    """calcula e retorna a quantidade máxima de bolos que João consegue fazer, dados as quantidades de xícaras de farinha de trigo A, ovos B e colheres de sopa de leite C"""
    return min(A//2,B//3,C//5)