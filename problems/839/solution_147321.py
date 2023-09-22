from math import ceil
def viagem(pessoas):
    """Calcula a quantidade de carros necessários
       para transportar x passsageiros; int->int"""
    return ceil(pessoas/5)