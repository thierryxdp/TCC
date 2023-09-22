def fatorial(n):
    '''função que retorna o fatoraial de um numero'''
    '''int -> int'''
    contador = 0
    n = int(n)
    while contador <= n:
        if n == 0 or n ==1:
            return 1
        if n > 1:
            contador -= 1
            n = n * (n-1)
	return n