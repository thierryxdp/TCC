def fatorial(numero):
    fatorial = 1
    for valor in list(range(numero + 1)):
        if valor != 0:
        	fatorial = fatorial * valor
    return fatorial