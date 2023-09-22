from math import floor, ceil

#EX2
def carros(num_pessoas,capacidade = 5):
    """
    Função que calcula o número exato de carros necessários para uma viagem, tendo como entrada:
    O número de pessoas para a viagem e a capacidade do veículo, considerando que todos os veículos são iguais.
    Caso a capacidade do veículo não seja dada, é considerada a capacidade de um veículo convencional(5).
    """
    return ceil(num_pessoas/capacidade)