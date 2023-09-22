def bolos(A,B,C):
    """calcula e retorna o numero maximo de bolos que Joao consegue fazer com A xicaras de farinha de trigo, B ovos e C colheres de sopa de leite;
    float, float, float -> int"""
    return min(A/2,B/3,C/5)