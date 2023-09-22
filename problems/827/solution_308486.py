def qtd_divisores(numero):
    '''
    	Funcao que calcula quantos divisores um numero tem
        int -> int
    '''
    divisores = 0
    x = list(range(1, numero))
    for i in x:
    	if numero%x[i-1] == 0:
            divisores += 1
    return divisores