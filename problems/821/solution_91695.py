def fatorial(num):
    """Retorne o fatorial de um numero dado por parametro;
    int -> int"""
    acum = 1
    cont = 1
    while cont < num:
        acum = acum*cont
        cont += 1
	return acum