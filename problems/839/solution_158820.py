import math
def carros(pessoas):
    """calcula quantos carros serão usados na viagem, sabendo que cada carro cabe 5 pessoas"""
    return math.ceil(pessoas/5)