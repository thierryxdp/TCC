def bolos(A,B,C):
    """calcula a quantidade de bolos que é possível fazer com
    A xícaras de farinha de trigo, B ovos e C colheres de sopa
    int, int, int -> int"""
    return min(A//2,B//3,C//5)