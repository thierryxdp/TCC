def carros(x):
    """ Calcula o número de carros (:int) necessários para transportar o número(n: int) de
pessoas em cada veículo. Se x<= 5, 1 carro necessário; se x> 5, usar x//5"""
    if x<=5:
        return 1
    if x>5:
        return x//5