import math
def carros(numero_de_pessoas,capacidade_do_veiculo):
    '''Função que recebe o número de pessoas e a capacidade 
    do veículo e calcule e retorne a quantidade de carros 
    necessários para a viagem;
    int,int ->int'''
    numero_de_carros = math.ceil(numero_de_pessoas/capacidade_do_veiculo)
    return numero_de_carros