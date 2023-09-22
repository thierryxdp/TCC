import math
def bolos(A,B,C):
    """Função que calcula e retorna o número de bolos, dados os números de xícaras, ovos e colheres."""
    return (math.gcd(B//3,C//5))