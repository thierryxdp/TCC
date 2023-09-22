def qtd_divisores(numero):
    '''Função que conta quantos divisores um numero N dado como parâmetro possui.
    int -> tupla'''
    divisores = ()
    i = 0
    contagem = range(0,numero+1)
    
    while i < contagem:
        if numero % contagem[i] == 0:
            divisores += (contagem[i]),
	return divisores