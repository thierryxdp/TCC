import math
def bolos(A,B,C):
    ''' Função para fazer bolo onde as entradas A,B,C informam a quantidade de xicaras de farinha de trigo, ovos e colheres de sopa de leite respectivamente. A receita indica que devem ser usadas 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite.'''
    X=math. floor(A/2)
    Y=math. floor(B/3)
    Z=math. floor(C/5)
    return min(X,Y,Z)