def bolos(A, B, C):
    """Determina a quantidade ḿaxima de bolos que João consegue fazer dados
    as quantidades de farinha A, ovos B e leite C que ele tem"""
    xicaras_de_farinha = A//2
    quantidade_de_ovos = B//3
    colheres_de_leite = C//5
    return min(xicaras_de_farinha, quantidade_de_ovos, colheres_de_leite)