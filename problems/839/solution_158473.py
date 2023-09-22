import math
def carros (pessoas, capacidade=5):
    '''funcao que calcula a quantidade de carros necessarios a 
  		partir da capacidade dita
        pessoas: int, float -> pessoas
    '''
	return math.ceil(pessoas/capacidade)