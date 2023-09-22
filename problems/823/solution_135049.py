def faltante(lista):
    i = 1
    listaNum = list(range(10000)
    while i<len(listaNum):
        if listaNum[i] not in lista:
        	return i
        i = i+1