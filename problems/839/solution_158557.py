import math
def carros(p,cap=5):
    """Função que calcula o número exato de carros necessarios para uma viagem, dado o número de pessoas, tendo em vista que cada carro tem a capacidade de levar 5 passageiros no máximo. int,int -> int"""
    return math.ceil(p/cap)