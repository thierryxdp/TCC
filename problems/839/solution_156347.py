def carros(p,c=5):
    """Tem como objetivo descobrir quantos carros são 
    necessários para uma viagem ser feita com relação ao 
    de passageiros. int > int"""
    carros = from math import ceil(p/c)
    return carros