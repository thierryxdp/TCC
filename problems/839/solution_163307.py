from math import ceil
def carros(numero_de_pessoas,capacidade = 5):
    quantidade_de_carros = ceil(numero_de_pessoas//capacidade)    
    return quantidade_de_carros