import math
def carros(x,y):
    """Calcula o número de carros x necessários para a viagem dos amigos
    Caso os veículos possuam capacidades não convencionais, será dado também como
    entrada a capacidade diferente dos veículos, considerando que todos os 
    são iguais"""
    if y=5:
        return math.ceil(x/5)
    else: 
        return math.ceil(x/y)