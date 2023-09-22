def fatorial(numero):
    '''
    Função que dado um número inteiro, calcula o fatorial 
    deste número
    '''
    numero >= 0
    resultado = 1
    x = 1
    while x <= numero:
    	resultado = resultado * x
    	x = x + 1

	return resultado