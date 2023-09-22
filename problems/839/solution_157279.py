def carros(p,n=5):
    # p= numeros de pesssoas na viagem, n= numero de pessoas por carro, a função retorna o número de carros necessários pra essa viagem
	import math.ceil
    return math.ceil(p/n)