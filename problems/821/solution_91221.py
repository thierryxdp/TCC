def fatorial(n):
    '''
    Função que dado um número inteiro, calcula o fatorial deste número
    int->int
    '''
    n>=0
    resposta = 1
    x = 1
    while x <= n:
    	resposta = resposta*x
    	x = x + 1

	return resposta