def maiores(ls,n):
    list.sort(ls)
    if(n not in ls):
    	return []
    pos=list.index(ls,n)
    return ls[pos+1: ]