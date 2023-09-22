import math
def carros(p,c):
    """função que calcula e retorna a quantidade exata de carros necessários
    para acomodar todas as pessoas numa viagem a partir do número de pessoas "p" e a capacidade total do carro "c"
    int,int->int"""
    return math.ceil(p/c)