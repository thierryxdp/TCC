import math
def carros(p, c=5):
    """Calcula a quantidade de carros necessárias para realizar a viagem, c recebendo o valor default de 5 pessoas, e p a quantidade de pessoas"""
    return math.ceil(p/c)