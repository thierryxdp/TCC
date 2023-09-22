def maiores(ls,n):
    list.sort(ls)
    if(n in ls):
    	return ls[list.index(ls,n)+1:0]
    return []