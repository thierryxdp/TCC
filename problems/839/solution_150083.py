import math

def carros(p,c=5):
    """função que calcula e retorna o número de carros necessários para uma viagem
    através do quociente entre o número de pessoas p e a capacidade do veículo c;
    int,int -> int"""
    return math.ceil(p//c)