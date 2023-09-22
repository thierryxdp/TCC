import math

def bolos(A,B,C):
    """Calculo quandos bolos podem ser feitos com A xícaras de farinha, B ovos,
    C colheres de sopa de leite. Considerando a receita 2 xícaras de farinha,
    3 ovos e 5 colheres de sopa de leite.(int,int,int->int)"""
    a=math.floor(A/2)
    b=math.floor(B/3)
    c=math.floor(C/5)
    return min(a,b,c)