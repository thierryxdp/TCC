def qtd_divisores(x):
    """ A função conta quantidade de divisores um número tem"""
    r = 0
    for i in range(x):
        if x%(i+1) == 0:
            r = r + 1
	return r