def maiores(ls,n):
    for e in ls:
        if e<n:
            list.remove(ls,e)
    		list.sort(ls)
    return ls