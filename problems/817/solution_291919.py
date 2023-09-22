def acima_da_media(l):
    n = sum(l)/len(l)
    list.append(l,n)
    list.sort(l)
    i = list.index(l,n)
    l2 = set(l)
    l3 = list(l2)
    return l3