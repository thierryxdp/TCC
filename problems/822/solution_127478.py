def repetidos(lista):
    count = 0
	for i in range(1,len(lista)):
		if lista[i] == lista[i-1]:
            count += 1
	return count