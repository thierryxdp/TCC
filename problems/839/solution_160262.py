import math
def carros(passageiros,lugares=5):
    'Função que diz o número de carros para uma certa quantia de passageiros. Caso não haja input de lugares, o valor padrão é 5.'
    return math.ceil(passageiros/lugares)