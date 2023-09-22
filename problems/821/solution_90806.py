def fatorial(num):
    '''Função que pega o número de entrada, e retorna o seu fatorial 
    in, int→int'''
	if num ==0:
        return 1
    else:
        fact=1
        while(num>1):
            fact *= num
            num -= 1
		return fact