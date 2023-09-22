def acima_da_media(l):
    n = sum(l))/len(l)
    l2 = l[:]
    list.append(l2, n) 
    list.sort(l2)
    i = list.index(l2, n)
    return l2[i:]