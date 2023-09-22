def repetidos(lista):
    cont = 0
    for x in lista:
        for y in range(len(lista)):
            if x[y] == x[y-1]:
                cont += 1
	return cont