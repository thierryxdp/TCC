import math 

def carros (pessoas, capacidade = 5):
    """Define a quantidade de carros necessários tendo como entrada o número de pessoas"""
    return math.ceil(pessoas/capacidade)