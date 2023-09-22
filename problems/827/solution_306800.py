def qtd_divisores(numero):
    '''funcao que retorna a quantidade de divisores que o numero dado possui.
	int -> int'''
    divisores = 0
    for num_divisor in list(range(1,numero)):
        if numero % num_divisor==0:
            divisores += 1
    return divisores