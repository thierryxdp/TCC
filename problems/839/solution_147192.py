import math

def carros(pessoas, capacidade=5):
    """Calcula a quantidade de carros necessários para uma viagem dado o número de pessoas.
    Também é dada a capacidade do carro caso sejam não convencionais, ou seja, se os carros
    tiverem capacidade diferente de 5 passageiros.
    int, int -> int"""
    return math.ceil(pessoas/capacidade)