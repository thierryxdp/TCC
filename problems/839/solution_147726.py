import math
def carros(x,y=5):
    """funçao que calcula e retorna a quantidades de carros que são necessarios para uma viagem dados o números de pessoas x e a capacidade por carro y como entradas do problema.
    Caso não seja dado nenhum valor para y, este assumirá o valor de 5 passageiros por carro; int, int -> int"""
    return math.ceil(x/y)