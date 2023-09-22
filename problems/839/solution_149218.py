def carros(pessoas,capacidade=5):
    '''Calcula a quantidade de carros ecessária para transportar determinado
    número de pessoas, dada a sua quantidade e a capacidade do carro. Caso não
    seja informada a capacidade do veículo, será considerada a capacidade convencional,
    de 5 pessoas.
    int,int -> '''
    if pessoas%capacidade==0:
        return pessoas//capacidade
	else:
     	return(pessoas//capacidade)+1