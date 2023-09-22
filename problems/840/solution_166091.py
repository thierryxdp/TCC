def bolos(A,B,C):
    """função que retorna o numero de bolos que joao consegue fazer com A xícaras de farinha, B ovos e C colheres de sopa de leite"""
    return min(A//2,B//3,C//5)