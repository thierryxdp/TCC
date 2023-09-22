def acima_da_media(l):
    ''
	list.sort(l)
    s=sum(l)
    m=(s)/len(l)
    l= l + [m]
    p=l.index(m)
    l=l[p:] 
    l.pop(0)
    return m