import math
def carros(p,c=5):
    """calcula quantos veiculos sao necessarios para fazer uma viagem dependendo do numero de pessoas(p), a capacidade do veiculo é definida por(c)""""
    return math.ceil(p/c)