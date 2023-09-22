def acima_da_media(l):
	media = sum(l)/(1.0*len(l))
	aprovados = maiores(l,media)
	return aprovados