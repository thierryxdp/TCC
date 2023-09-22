def fatorial(n):
    '''Cacula o fatorial de n.
    int --> int'''
    i = n
    j = 1
    resultado = 0
    while i > 0:
        j = j * (j+1)
        if i == n:
            j = 1
        i -= 1
        
	return j