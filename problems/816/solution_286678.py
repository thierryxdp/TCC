def maiores(ls,n):
    list.sort(ls)
    if( n not in ls):
    	return []
    return ls[list.index(ls,n)+1:0]