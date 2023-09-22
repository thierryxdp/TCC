import math
def bolos(a,b,c):
    "Definie o número máximo de bolos que se pode faser com a xícaras de farinha de trigo, b ovos e c colheres de sopa de leite."
    return min(a//2, b//3, c//5)