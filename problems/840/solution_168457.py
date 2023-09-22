#Questao 3
def bolos(A, B, C):
    '''
Funcao que determina qual a quantidade maxima de bolos que Joao consegue fazer.
Sendo A=xicaras de farinha de trigo, B=ovos e C=colheres de sopa de leite.
int int
    '''
    if (A >= 2):
        return A // 2
    elif (B >= 3):
        return B // 3
    elif (C >= 5):
        return C // 5
    else:
        (A +B+ C)=1