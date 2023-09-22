def bolos(A,B,C):
    """Calcula a quantidade maxima de bolos dada as medidas dos ingredientes,
    sendo: A xicaras de farinha de trigo, B numeros de ovos
    e C colheres de sopa de leite"""
    return min(A//2,B//3,C//5)