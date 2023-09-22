import math 
def carros(pessoas, veic=5):
    ''' calcula o número de carros necessários para uma viagem, com base no número de pessoas, 
    tendo em vista que um veículo convencional tem capacidade de transportar 5 pessoas '''
    return math.ceil pessoas/veic