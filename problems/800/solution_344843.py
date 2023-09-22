def total(lista, preco):
	precos = []
    for i in lista:
        if i in dict.keys(preco):
            preco.append(preco[i])
    return round(sum(precos),2)