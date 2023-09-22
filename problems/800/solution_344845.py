def total(lista, preco):
	precos = []
    for i in lista:
        if i in dict.keys(preco):
            precos.append(preco[i])
    return round(sum(precos),2)