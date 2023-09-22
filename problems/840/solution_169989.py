import math
def bolos(A,B,C):
    """função que retorna o número máximo de bolos possíveis de se fazer com A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite de entrada"""
    return min(A//2,B//3,C//5)