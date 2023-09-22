def fatorial(num):
    '''Função que receba como entrada um número retorne o 
    fatorial do mesmo. int --> float.'''
    fatorial = 1
    a = 1
    while a <= num:
        fatorial = fatorial*a
        a = a+1
    	return fatorial