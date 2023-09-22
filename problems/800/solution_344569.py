def total(list, prods):
    soma=0
    x=0
    while x<len(list):
        soma+=prods[list[x]]
        x+=1
	return round(soma, 2)