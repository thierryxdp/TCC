import math
def carros (p,c=5):
    """Calcula o valor de carros a serem utilizados numa viagem, sobre as regras rodoviarias."""
    """Dados o número de passageiros e a quantidade de pessoas suportadas por ele, onde caso não haja um valor para a quantidade de pessoas suportadas, consideraremos um veículo convencional de 5 passageiros."""
    """Faremos o cálculo do número de pessoas dividido pela capacidade suportada pelo veículo, caso seja um valor real, aproximaremos para o menor inteiro maior que o valor real atribuido na divisão."""
    return math.ceil (p/c)