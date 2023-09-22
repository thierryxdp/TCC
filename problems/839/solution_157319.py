import math
def carros(numero_de_pessoas, capacidade_do_veiculo=5):
    return math.ceil(numero_de_pessoas//capacidade_do_veiculo)