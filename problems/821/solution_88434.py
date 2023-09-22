def fatorial(n):
    '''Cacula o fatorial de n.
    int --> int'''
    i = n
    j = 1
    while i > 0:
        j = j * (j+1)
        i -= 1
        
	return j