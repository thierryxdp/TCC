def maiores(ls,n):
    list.append(ls,n)
    list.sort(ls)
    pos=list.index(ls,n)     
	return ls[pos+1:]

def acima_da_media(ls):
    if(med=sum(ls)):
    	return[]
    med=sum(ls)/len(ls)
    return maiores(ls,med)