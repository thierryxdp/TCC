def total(lista, preco):
    gasto = 0
    for produtos in lista:
        if produtos in preco:
            gasto = gasto + dict.get(preco,produtos)
	return round(gasto, 2)