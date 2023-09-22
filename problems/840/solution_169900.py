import math
def bolos(A,B,C):
    "Calcula a quantidade maxima de bolos a ser feito dado a receita padrao"
    bolos=(2*A)+(3*B)+(5*C)
    x=A/2
    y=B/3
    z=C/5
    return floor(min(x,y,z))