from math import ceil
def carros (x, y):
    """calcula a quantidade de carros necessária para a viagem"""
    def capacidade (y):
        return (x/y)