def maiores(l, n):
    if n not in l:
        list.insert(l,0,n)
    list.sort(l)
    
    f = list.index(l,n)
    l2 = l[f+1:]
    
    return l2
    
def acima_da_media(n):
    x=sum(n)/len(n)
    return maiores(nx)