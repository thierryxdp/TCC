def maiores(ls,n):
    list.sort(ls)
    if( n in ls):
    	return list.index(ls,n)
    return []