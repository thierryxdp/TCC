def acima_da_media(l):
    ''
    s=sum(l)
    m=(s)/len(l)
    l= l + [m]
    list.sort(l)
    p=l.index(m)
    l=l[p:]
    list.remove(l,m)
    if m==l[0]:
        return []
    else:
        return l