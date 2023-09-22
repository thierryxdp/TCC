from math import ceil
def carros(numero_de_pessoas,capacidade = 5):
    quantidade_de_carros = (numero_de_pessoas//capacidade).ceil    
    return quantidade_de_carros