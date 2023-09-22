def faltante(x):
    r = len(x)
    i = 0
	for teste in range(1, r):
        if x[i] == teste:
        	i = i + 1
        elif x[i] != teste:
            return teste
        else:
            return len(x+1