#list-->list
#dado uma lista de notas retorna uma nova lista apenas com as notas que ficara acima da média dessa lista original
def acima_da_media(j):
	l=sum(j)
	m=l/len(j)
	k=[]
	for x in j:
		if x>m:
			list.append(k,x)
	list.sort(k)
	return k