def acima_da_media(l):
    n = sum(l)/len(l)
    l2 = l[:]
    list.sort(l2)
    i = list.index(l2,n)
    l3 = l2[i:]
    return l3