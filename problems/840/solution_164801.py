import math
def bolos(A,B,C):
    "funcao que define a quantidade de bolos possiveis dadas as quantidades dos ingredientes especificos A, B e C. respectivamente xicaras de farinha de trigo, ovos e colheres de leite."
    return math.floor (((A/2)+(B/3)+(C/5))/3)