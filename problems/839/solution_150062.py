import math

def carros(p,c=5):
    """função que calcula e retorna o número de carros necessários para um viagem
    através do qupciente entre o número de pessoas p e o número de passageiros no 
    veículo c; int,int -> int"""
    return math.ceil(p/c)