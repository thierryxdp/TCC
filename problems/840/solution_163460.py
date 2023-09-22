from math import floor
def bolos(A,B,C):
    """função que define a quantidade máxima de bolos que uma pessoa pode fazer considarando a quantidade A de xicaras de farinha, B de ovos e C de colheres de sopa de leite"""
    X=A/2
    Y=B/3
    Z=C/5
    return floor(min(X,Y,Z))