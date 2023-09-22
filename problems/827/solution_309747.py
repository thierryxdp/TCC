def qtd_divisores(n):
	'''
    '''
    i=0
    for caractere in range(1, n+1):
        if n%caractere==0:
        i=i+1
    return i