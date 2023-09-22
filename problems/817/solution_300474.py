def acima_da_media(l):
    ''
    s=sum(l)
    m=(s)/len(l)
    l= l + [m]
    list.sort(l)
    p=l.index(m)
    l=l[p:] 
    l.pop(0)
    return l