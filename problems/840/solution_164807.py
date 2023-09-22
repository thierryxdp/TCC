def bolos(A,B,C):
    """Calcula a quantidade máxima de bolos que João consegue fazer,
    dados os números de xícaras de farinha de trigo A, ovos B e colheres 
    de sopa de leite C"""
    return min(A//2,B//3,C//5)