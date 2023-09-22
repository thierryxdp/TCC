def maiores(ls,n):
    list.sort(ls)
    pos=list.index(ls,n)
    if(n not in ls):
    	return []
    return ls[pos+1:]