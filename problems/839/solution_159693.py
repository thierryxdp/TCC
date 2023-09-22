from math import ceil
def carros(pessoas,capacidade=5):
    '''calcula a quantidade de veículos necessários para a realização de uma viagem, dado o número de pessoas que farão a viagem e, caso seja diferente de um veículo convencional, a sua respectiva capacidade'''
	return ceil(pessoas/capacidade)