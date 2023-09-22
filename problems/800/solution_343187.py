def total(lista,produtos):
    '''
    '''
	pro=list(dict.keys(produtos))
    t=0
    for i in lista:
        for j in pro:
            if i == j:
                t=t+produtos[j]
	return t