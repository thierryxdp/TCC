def carros(num_pessoas, capacidade=5):
    '''dado o numero de pessoas, calcula o numero de carros necessarios para realizar a viagem,
    considerando como argumento default a capacidade convencional de um carro de 5 pessoas'''
    	return (num_pessoas // capacidade) + 1