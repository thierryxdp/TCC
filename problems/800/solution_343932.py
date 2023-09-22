def total(comprar, produtos):
    r = 0
    i = 0.0
	for x in comprar:
        if x in produtos:
            i = i + dict.get(produtos, x)
	return i