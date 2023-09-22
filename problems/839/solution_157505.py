import math
def carros (numero_pessoas, espaco_veiculo=5):
    '''função para calcular a quantidade de carros necessários
    de acordo com o número de pessoas e a quantidade de espaços
    no veículo'''
    '''(int, int => int)'''
    return math.ceil(numero_pessoas / espaco_veiculo)