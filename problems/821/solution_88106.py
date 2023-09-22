def fatorial(num):
    '''Função que receba como entrada um número retorne o 
    fatorial do mesmo. int --> float.'''
    fat = 1
    a = 1
    while a <= num:
        fat = fat*a
        a = a+1
    	return fat