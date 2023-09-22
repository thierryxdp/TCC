def fatorial(numero):
    """Funcao que calcula o fatorial do numero da entrada. int->int"""
	fact = 1
    cont = 1
    while cont <= numero:
        fact = fact*cont
        cont = cont + 1
    return fact