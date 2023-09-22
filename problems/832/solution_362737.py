def eh_quadrada(m):
	i = len(m)
    j = len(m[1])
    for n in m:
        if i == j:
            return True
        if i!= j:
            return False
        if m == []:
            return True