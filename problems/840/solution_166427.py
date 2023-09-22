import math
def bolos(A,B,C):
    """Calcula e retorna o numero maximo(inteiro) de bolos dados os coeficientes de entrada,
    indicando respectivamente o numero A de xicaras de farinha de trigo,o numero de ovos e numero de colheres de sopa de leite"""
   return math.floor(min(A/2,B/2,C/5))