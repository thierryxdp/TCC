def total(comprar, produtos):
    i = 0.0
	for x in comprar:
        if x in produtos:
            i = i + dict.get(produtos, x)
	return round(i, 2)