def fatorial(n):
    '''calcula o fatorial de um numero.
    int->int'''
    fatorial = 1
    i = 2
    while i <= n:
        fatorial = fatorial*i
        i = i + 1
	return fatorial