from math import ceil
def carros(pessoas):
    """Calcula a quantidade de carros necessários
       para transportar x passsageiros; int->int"""
    return ceil(pessoas/5)