import math
def carros(pessoas,capacidade=5):
    carro=math.ceil(pessoas/capacidade)
    '''
    	Funcao que calcula a quantidade de carros necessaria
        para certo numero de pessoas dividido pela capacidade
        do carro
        	int, int -> int
    '''
    return carro