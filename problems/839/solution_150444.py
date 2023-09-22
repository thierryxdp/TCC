import math
def carros(x,y=5):
    """calcula o numero minimo de veiculos a serem utilizados para transportar todos os passageiros, de acordo com a capacidade do veiculo, sendo o padrao 5 lugares, em que x é o numero de passageiros e y o numero de lugares"""
    return math.ceil(x/y)