def repetidos(l):
	c = 0
    i = 0
    while i <= len(l):
        if l[i] == l[i-1]:
            c += 1
        i += 1
    return c