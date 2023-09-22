import math
def carros(pessoas,capacidade=5):
    '''Calcular quantos veiculos ser necesssario para um grupo de amigos
    dividindo pela capacidade do veiculo por lei
    flout,flout->int'''
    return math.ceil(pessoas/capacidade)