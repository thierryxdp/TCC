def qtd_divisores(numero):
    '''Função que conta quantos divisores um numero N dado como parâmetro possui.
    int -> tupla'''
    divisores = ()
    for a in range(0,numero+1):
        if numero % numero[a] == 0:
            divisores += (numero[a]),
	return divisores