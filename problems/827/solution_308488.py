def qtd_divisores(numero):
    '''
    	Funcao que calcula quantos divisores um numero tem
        int -> int
    '''
    divisores = 0
    for i in range(1, numero):
    	if numero%i == 0:
            divisores += 1
    return divisores