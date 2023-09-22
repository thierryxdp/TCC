from math import*
def carros (p,c)
    """Função que calculara o número de carros necessário para a viagem. Caso a capacidade não seja informada, levaremos em consideração a capacidade de 5 pessoas"""
    return math.ceil(p//c)