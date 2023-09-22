def maiores(ls,n):
    list.append(ls,n)
    list.sort(ls)
    pos=list.index(ls,n)     
	return ls[pos+1:]

def acima_da_media(ls):
    med=sum(ls)/len(ls)
    list.remove(ls,med=len(s))
    return maiores(ls,med)