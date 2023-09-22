from math import ceil

def carros (passageiros, capacidade=5):
    """calcula a quantidade necessária de carros para fazer uma viagem com um determinado número de passageiros.
       Caso a capacidade do veículo não seja informada, o número considerado será 5, capacidade convencional.
       int, int -> int"""
    return ceil(passageiros/capacidade)