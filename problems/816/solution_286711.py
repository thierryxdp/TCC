def maiores(ls,n):
    list.sort(ls)
    if (n in ls):
        return True
    return ls[list.index(ls,n)+1:]
    
    return[]