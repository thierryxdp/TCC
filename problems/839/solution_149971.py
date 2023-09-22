def carros(p,c=5):
    """retorna o valor exato de carros que serao utilizados numa viagem dado a quantidade de passageiros e a capacidade do carro, se nao for informada sera considerada um valor padrao de 5 lugares"""
    import math
    x = p / c
    return math.ceil(x)