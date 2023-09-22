def qtd_divisores(numero):
    '''função que retorna a quantidade de divisores de um número
    float --> int'''
    qtd_div=0
    for i in range(1, numero+1):
        if numero % i == 0:
            qtd_div = qtd_div+1
	return qtd_div