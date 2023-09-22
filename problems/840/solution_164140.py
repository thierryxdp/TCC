def bolos(A, B, C):
    """define a quantidade maxima de bolos que joao pode fazer dados o numero de xicaras de farinha de trigo, o numero de ovos e o numero de colheres de sopa de leite que joao tem em cas
    int, int, int --> str"""
    return min(A//2,B//3,C//5)