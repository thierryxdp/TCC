def carros(p,c):
    """calcula e retorna o numero de carros necessarios para levar um grupo de pessoas, dado que p, seja para passageiros e c, para a capacidade total do carro"""
    return math.ceil(p/c)