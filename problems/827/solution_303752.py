def qtd_divisores(n):
    '''função que retorna o numero de divisores que um numero tem'''
    '''int->int'''
    divisores = 0
    for divisores in range(n):
        if (n%divisores)==0:
            divisores+=1
	return divisores