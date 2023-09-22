def total(comprar, produtos):
    i = 0
	for x in produtos:
        if comprar[i] in produtos:
            i = i + dict.get(produtos, comprar[i])

	return i