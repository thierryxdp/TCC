import math
# int, int, int -> int
def bolos(A,B,C):
    """Dados o número de xícaras de farinha de tigo 'A', o número 'B' de ovos e o número
    'C' de colheres de sopa de leite, a função retornará a quantidade máxima de bolos que
    podem ser confecionados"""
    X = A/2
    Y = B/3
    Z = C/5
    return math.floor(min(X,Y,Z))