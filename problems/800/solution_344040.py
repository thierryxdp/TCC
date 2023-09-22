# Dado uma lista de compras e um dicionário contendo os preços retorna o valor total da compra
# list,dic-->float
def total(ls,dic):
	y=0
	for x in ls:
		y=y+dic[x]
	return round(y,2)