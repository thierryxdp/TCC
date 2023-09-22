def acima_da_media(l):
    n = round(sum(l)/len(l))
    l2 = l[:]
    list.append(l2,n)
    list.sort(l2)
    i = list.index(l2,n)
    l3 = l2[i+1:]
    return l3