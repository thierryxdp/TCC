def fatorial(n):
    """ dado um número 'n', retorna o fatorial deste número.
    int->int """
    resultado=1
	count=1

	while count <= n:
    resultado = resultado*count
    count += 1
    
    return resultado