def fatorial(num):
    '''retorna a fatorial de um numero;
    int->int'''
    fac = 1
    i = 1
 
    while i <= num:
	    fac = fac * i
	    i = i + 1
    return fac