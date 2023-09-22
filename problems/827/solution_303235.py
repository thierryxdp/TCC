def qtd_divisores(numero):
    '''Função que conta quantos divisores um numero N dado como parâmetro possui.
    int -> tupla'''
    divisores = ()
    i = 0
    
    while i < range(0,numero):
        if numero % i == 0:
            divisores += (i),
       	i=i+1
	return divisores