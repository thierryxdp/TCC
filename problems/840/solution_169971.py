def bolos(A,B,C):
    """Função que calcula a quantidade máxima de bolos que consegue fazer com A xícaras de farinha, B ovos e C colheres de sopa de leite"""
    return min(A//2,B//3,C//5)