def maiores(m,n):
    list.append(m,n)
    list.sort(m)
    a=list.index(m,n)
    s=m[a+1:]
    return s

def acima_da_media(q):
    w=sum(q)/len(q)
    return maiores(q,w)