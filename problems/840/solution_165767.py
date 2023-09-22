from math import max
def bolos(A,B,C):
    ''' funcao recebe 3 valores, A,B e C, onde "A" e a quantidade de xicaras de farinha de trigo,"B" quantidade 
    de ovos e "C" quantidade de colheres de sopa de leite. A partir desses valores delvolve
    a quantidade max de bolos capazes de produzir com esses ingredientes'''
    return max(A//2,B//3,C//5)