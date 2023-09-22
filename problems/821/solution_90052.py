def fatorial(numero):
    #função que retorna fatorial de um número
    #int -> int
	total = 1
    contador = 2
    while contador <= numero:
        total = total * contador
        contador = contador+1
    return total