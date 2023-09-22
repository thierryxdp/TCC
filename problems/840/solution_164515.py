def bolos(A,B,C):
    """Calcula a quantidade maxima de bolos que se consegue fazer usando as medidas exatas da receita
    int, int, int -> float"""
    return min((A//2),(B//3),(C//5))