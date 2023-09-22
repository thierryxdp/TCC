import.math
def carros (x,y=5):
    """calcula o num de carros necessários para um número x de pessoas em virtude da capacidade do veiculo default(5)"""
    return math.ceil(carros(x//y))