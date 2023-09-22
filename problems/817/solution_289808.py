def acima_da_media(lis):
	k=sum(lis)/len(lis)
	list.insert(lis,0,k)
	list.sort(lis)
	loc=list.index(lis,k)
	if k in list:
		lis3=lis[loc+1:]
		lis2=list.remove(lis3,k)
		return lis2
	else:
		return lis[loc+1:]