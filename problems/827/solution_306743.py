def qtd_divisores(numero):
    ''' Dada um numero como entrada, retorna a quantidade
    de divisores que ele possui'''
    i = 0
    for x in range(numero):
        if numero % x == 0:
    		i += 1
  	return i