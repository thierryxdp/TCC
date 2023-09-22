def repetidos(lista):
    i = i2= ni = n2 = 0
    while i <= len(lista):
        n1 = lista[i]
        n2 = lista[i + 1]
        if n1 == n2:
            i2 += 1
            i += 1
        i += 1
	return i2