def fatorial(n):
    '''
    Função que dado um número inteiro, calcula o fatorial deste número
    '''
    n>=0
    resultado = 1
    x = 1
    while x <= n:
    	resultado = resultado*(x)
    x = x + 1

	return resultado