def total(comprar, produtos):
    i = 0
    r = 0
	for x in produtos:
        if comprar[r] in produtos:
            i = i + dict.get(produtos, comprar[i])
            r = r + 1

	return i