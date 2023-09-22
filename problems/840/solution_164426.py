from math import floor
def bolos(A,B,C):
    """Retorna a quantidade máxima de bolos que se pode fazer com uma determinada quantidade de xícaras de farinha como o primeiro valor de entrada, ovos como o segundo valor de entrada e colheres de sopa de leite como terceiro valor de entrada;
    float,float,float->int"""
    return floor(A/2,B/3,C/5)