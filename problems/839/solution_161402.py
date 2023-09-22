import math
def carros (pessoas,capacidade=5):
    """calcula a quantidade de carros necessarios para fazer uma viagem, dado como entrada a quantidade de pessoas(int) e a capacidade do veiculo(int), caso capacidade não seja informada, sera considerado um veiculo convencional que comporta o total de 5 pessoas"""
    return math.ceil(pessoas/capacidade)