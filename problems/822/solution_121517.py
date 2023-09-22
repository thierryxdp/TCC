def repetidos(num):
    i, cont = 0, 0
    while i < len(num) - 1:
        if num[i] == num[i + 1]:
            cont += 1
		i += 1
	return cont