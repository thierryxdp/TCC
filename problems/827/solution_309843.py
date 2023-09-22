def qtd_divisores(n):
    '''função que conta o número de divisores que um número n possui;
    int->int'''
    qtd = 0
    for divisor in range(1,1+n):
    	if n%divisor==0:
            qtd += 1
        else:
            qtd = qtd
    return qtd