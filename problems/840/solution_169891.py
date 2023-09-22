import math
def bolos(A=2,B=3,C=5):
    "Calcula a quantidade maxima de bolos a ser feito dado a receita padrao"
    return math.floor(A/2)+(B/3)+(C/5)