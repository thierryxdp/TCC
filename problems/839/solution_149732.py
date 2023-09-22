from math import *
def carros(passageiros,capacidade=5):
    """Será dividida a quantidade de passageiros pela capacidade de cada carro
    com o objetivo de calcular o número exato de carros para todos realizarem
    a viagem. Caso a capacidade não seja especificada, a mesma apresentará
    o valor cinco relativo ao numero convencional de capacidade de veicúlos segungo
    as regras da rodoviária."""
    return ceil(passageiros/capacidade)