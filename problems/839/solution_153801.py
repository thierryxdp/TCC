import math
def carros(pessoas, capacidade = 5):
    '''
    calcula e retorna a quantidade de carros necessária para fazer uma viagem, dados o número de pessoa que farão a viagem e a capacidade de pessoas que o carro comporta caso não seja o convencional (5 pessoas);
    int, int -> int
    '''
    return math.ceil(pessoas/capacidade)