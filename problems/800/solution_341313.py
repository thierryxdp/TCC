def total(lista,preco):
    i = 0
    for item in lista:
        i += dict.get (preco,item,0)
	i = round(i,2)
    return i