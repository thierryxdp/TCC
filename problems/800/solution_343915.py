def total(comprar, produtos):
    i = 0.0
    r = 0
	for x in produtos:
        if comprar[r] in produtos:
            return dict.get(produtos, comprar[i])