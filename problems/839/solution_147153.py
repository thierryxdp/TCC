def carros(p, c=5):
    i = p//c
    j = p%c
    if j != 0:
        return i + 1
    else:
    	return i