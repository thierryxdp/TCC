import math 
def bolos(a,b,c):
    '''Retorna a quantidade de bolos que é possível
    fazer, dada a quantidade dos respectivos ingredientes'''
    receita = (a//2,b//3,c//5)
    return min (receita)