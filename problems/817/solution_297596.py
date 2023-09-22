def maiores(l,n):
    l.append(n)
    l.sort()
    a = l.index(n)
    b = l[a+1:]
    return b

def acima_da_media(l):
    a = sum(l)/len(l)
    b = maiores(l,a)
    return b