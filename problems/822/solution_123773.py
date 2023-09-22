def repetidos(lista):
    cont = 0
    for y in range(len(lista)):
    	if lista[y] == lista[y-1]:
        	cont += 1
	return cont