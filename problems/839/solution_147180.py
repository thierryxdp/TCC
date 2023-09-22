import math

def carros(pessoas, capacidade=5):
    """Calcula o número de carros necessários para uma viagem, dados o número de pessoa.
    A capacidade também será dada se os carros forem de capacidade não convencionais, ou
    seja, tenham uma capacidade diferente de 5 passajeiros.
    int, int -> int """
    return math.ceil(pessoas//capacidade)