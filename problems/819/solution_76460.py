def filtraMultiplos(lista,n):
	retorno=[]
    x=0
    while x < len(lista):
        if lista[x] % n == 0:
            retorno.append(lista[x])
            x = x + 1
        else:
			x = x + 1
        return retorno