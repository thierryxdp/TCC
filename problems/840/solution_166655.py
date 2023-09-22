def bolos(A,B,C):
    """calcula o numero maximo de bolos confeccionaveis, dados os numeros de xicaras de farinha de trigo, A, de ovos, B e de colheres de sopa de leite, C;
    int, int, int -> int"""
    return min(A//2,B//3,C//5)