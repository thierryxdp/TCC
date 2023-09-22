def eh_quadrada(m):
    i = 0
    while i < len(m)+1:
        l = m[i]
        if len(m) == len(l):
            r = True
		if len(m) != len(l):
            r = False
	return r