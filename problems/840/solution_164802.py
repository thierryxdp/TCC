import math 
def bolos(A,B,C):
    "funcao que define a quantidade de bolos possiveis dadas as quantidades dos ingredientes especificos A, B e C. respectivamente xicaras de farinha de trigo, ovos e colheres de leite."
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))