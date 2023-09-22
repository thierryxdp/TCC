def acima_da_media(l):
    ''
	list.sort(l)
    s=sum(l)
    m=(s)/len(l)
    l= l + [m]
    l=l[m:] 
    l.pop(0)
    return l