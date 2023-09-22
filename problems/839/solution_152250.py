import math

def carros (p,cv=5):
    """determina o número de carros necessários para uma
    viagem, dado o número de pessoas (p). no caso de 
    veículos de capacidade não convencional, essa deve
    ser especificada em (cv).
    int,int -> int"""
    x = p/cv
    return math.ceil(x)