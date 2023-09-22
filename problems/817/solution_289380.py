def acimda_da_media(l):
    m = sum(l)/len(l)
    l.append(m)
    l.sort()
    return l[l.index(m)+1:]