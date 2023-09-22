def maiores(ls,n):
    r=[]
    for e in ls:
        if e > n:
            r.append(e)
            
    return list.sort(ls)