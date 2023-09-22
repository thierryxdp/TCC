import math
def bolos (A,B,C):
    """ esta função calcula a quantidade exata de bolos que João pode
    fazer dado a quantidade 'A' de xícaras de farinha de trigo, 'B' de ovos
    e 'C' de colheres de sopa de leite. """
    return min(A//2,B//3,C//5)