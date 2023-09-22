import math
def carros(passageiros,vagas=5):
    """retorna o numero de carros necessarios para fazer uma viagem, dado o numero de
    passageiros e as vagas dos veiculos(possuindo um padrao de 5 vagas por carro)"""
    x = passageiros/vagas
    return math.ceil(x)