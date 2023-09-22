def acima_da_media(lis):
	k=sum(lis)/len(lis)
	list.insert(lis,0,k)
	list.sort(lis)
	loc=list.index(lis,k)
	lis2=list.remove(lis[loc+1:],k)
	return lis2