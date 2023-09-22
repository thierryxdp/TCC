def total(lista, preco):
	precos = []
    for i in lista:
        if i in dict.keys(precos):
            preco.append(precos[i])
    return round(sum(precos),2)