def bolos(A,B,C):
    """retorna a quantidade máxima de bolos que João consegue fazer com A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite"""
    a = A//2
    b = B//3
    c = c//5
    return min(a,b,c)