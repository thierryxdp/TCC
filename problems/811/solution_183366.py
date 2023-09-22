def colchao(medidas,h,l):
	"""Função em que dada uma lista medidas contendo a,b,c, dimensões de um colchão e h,l, altura e largura da porta de João"""
	a=medidas[0]
	b=medidas[1]
	c=medidas[2]
	return (a<h and b<l) or (b<h and a<l) or (c<h and a<l) or (a<h and c<l) or (c<h and b<l) or (b<h and c<l)