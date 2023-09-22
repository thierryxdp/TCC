def fatorial (n):
    '''calcula o fatorial do número n
    int -> int'''
    contador = 0
    fatorial = 1
    while contador < n:
        fatorial = fatorial * (n - contador)
		contador = contador + 1
	return fatorial