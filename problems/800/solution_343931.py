def total(comprar, produtos):
	for x in comprar:
        if x in produtos:
            return dict.get(produtos, x)