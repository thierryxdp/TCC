def fatorial(numero):
	total = 1
    contador = 2
    while contador <= numero:
        total = total * contador
        contador = contador+1
    return total