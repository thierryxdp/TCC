def qtd_divisores(x):
    r = 0
    for i in range(x):
        if x//(i+1) == 2:
            r = r + 1
	return r