def fatorial(n):
    lista = [n]
    while n != 1:
        n = n - 1
        lista += [n,]
    produto = 1
	for numero in lista:
    	produto *= numero
    return produto