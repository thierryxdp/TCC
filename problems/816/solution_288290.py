def maiores(l,n):
    
    list.sort(l)
    for c in l:
        if (c)>(n):
            l.append (c)
    return l