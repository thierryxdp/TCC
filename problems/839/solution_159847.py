import math
def carros(pessoas,assentos=5):
    "funcao que calcula o numero de carros para a viagem"
    carros = math.ceil(pessoas/assentos)
    return carros