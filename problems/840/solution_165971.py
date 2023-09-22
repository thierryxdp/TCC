import math
def bolos(A,B,C):
    """função que define a quantidade máxxima de bolos que podem ser feitos seguindo
    a quantidade exata dos ingredientes pedidos na receita a partir da quantidade de xicaras de farinha de trigo "A"
    quantidade de ovos "B" e o número de colheres de sopa de leite "C" disponíveis na cada de jõao
    int,int,int->int"""
    return math.floor(min((A/2),(B/3),(C/5)))