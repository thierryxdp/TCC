def qtd_divisores(n):
	'''função que retorna o numero de divisores que um numero tem'''
    '''int->int'''
    i = 1
    b = []
    for i in range(1, n+1):
        if n % i == 0:
            k = b.append(i)
    return len(b)