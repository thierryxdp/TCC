def carros(pessoas, capacidade = 5):
    '''função que dado um número de pessoas retorna quantos carros são
    necessários para a viagem'''
    if pessoas%capacidade != 0:
    	return round(pessoas//capacidade)+1
    else:
        return pessoas/capacidade