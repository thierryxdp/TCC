def fatorial(num):
    ''' Dado um número inteiro, retornará seu fatorial.
    	(int => int)'''
    
    i = num
    f = num
    while i != 1:
        f = f * (i-1)
        i = i - 1

    return f