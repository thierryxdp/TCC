def bolos(a,b,c):
    """calcula o número de bolos que é possível fazer
    com os valores de xícaras de farinha de trigo (a),
    ovos (b) e colheres de sopa de leite (c) disponíveis.
    float, float, float -> int"""
    x = a//2
    y = b//3
    z = c//5
    return min(x,y,z)