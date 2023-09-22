import math
def carros (pessoas, capacidade=5):
    '''funcao que calcula a quantidade de carros necessarios
    	para a viagem a partir da sua capacidade
        carros: int
        pessoas: int
        return: int
    '''
    return math.ceil(pessoas/capacidade)