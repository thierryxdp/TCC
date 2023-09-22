def total(lista,produtos):
    total = 0
    for item in lista:
        total += produtos[item]
	return round(total,2)