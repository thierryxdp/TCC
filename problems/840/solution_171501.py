def bolos(A,B,C):
    """Calcular a quantidade máxima de bolos que 
    consegue fazer, dados o numero de xicaras de farinha,
    o numero de ovos e o numero de colheres de leite"""
    return min(A//2,B//3,C//5)