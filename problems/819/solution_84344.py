def filtraMultiplos(lista, n):
    nlista = []
    x = len(lista)
    while x < len(lista):
        if lista[x]%n == 0:
            nlista += lista[x]
    	return nlista