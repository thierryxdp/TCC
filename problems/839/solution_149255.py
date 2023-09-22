import math
def carros(num_pessoas,cap_veiculos=5):
    '''função que dado os parametros de numero de pessoas e capacidade do veiculo, retorna o número exato de carros necessarios em uma viagem; int,int->int'''
    return math.ceil(num_pessoas/cap_veiculos)