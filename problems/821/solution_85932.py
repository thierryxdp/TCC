def fatorial(num):
	'''dado um numero, retorna o seu fatorial
    int -> int'''
    while num != 1:
        return num * fatorial(num - 1)