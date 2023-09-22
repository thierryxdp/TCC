def total(comprar, produtos):
    r = 0
    i = 0.0
	for x in produtos:
        if comprar[r] in produtos:
            i = i + dict.get(produtos, comprar[r])
            
	return i