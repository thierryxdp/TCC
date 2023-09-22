def faltante(x):
    r = len(x)
    i = 0
    p = 0
	for teste in range(1, r):
        if x[i] == teste:
        	i = i + 1
        elif x[i] != teste:
            p = p = teste
        elif x[len-1] != len+1:
            return len(x+1)