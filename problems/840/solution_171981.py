def bolos (A,B,C):
    """calcula e retorna a quantidade máxima de bolos que João consegue fazer com A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite.Paramentros de entrada:2,3,5"""
    return max(A/2+ B/3+C/5)