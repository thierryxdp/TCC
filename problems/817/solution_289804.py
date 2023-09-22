def acima_da_media(lis):
	k=sum(lis)/len(lis)
	list.insert(lis,0,k)
	list.sort(list)
	loc=list.index(lis,k)
	return lis[loc+1:]