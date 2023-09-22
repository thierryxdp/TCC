def fatorial(n):
    '''função que dada como entrada um número n, calcula e
    retorna o fatorial deste número
    int -> int'''
	resultado=0
    count=1
    while count <= n:
        resultado = resultado * count
        count = count + 1
	return resultado