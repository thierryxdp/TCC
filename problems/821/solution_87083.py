def fatorial(n):
    '''Calcula o fatorial de n(int->int)'''
    fat = 1
    while n > 1:
        fat = fat * n
        n=n-1
	return fat