def maiores(ls,n):
    list.sort(ls)
    pos=list.index(ls,n)
    if(n in ls):
    	return ls[pos+1: ]
    
    return []