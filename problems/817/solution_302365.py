def acima_da_media(j):
	l=sum(j)
	m=l/len(j)
	l=[]
	for x in j:
		if x>m:
			list.append(l,j)
	list.sort(l)
	return l