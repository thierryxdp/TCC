import math

def carros(passageiros:int) -> int:
    """Calcula o número de carros necessário para realizar uma viagem ao informar
    o total de passageiros, levando em conta o limite de 5 passageiros por carro"""

    return math.ceil(passageiros/5)