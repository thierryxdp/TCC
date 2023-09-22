import math
def carros(Np,Nm=5):
    """Número de carro necessários para Np pessoas e Nm vagas por carro"""
    return math.ceil(Np/Nm)