def acima_da_media(l):
    n =(sum(l)/len(l))
    list.sort(l)
    l3 = l[n:]
    return l3