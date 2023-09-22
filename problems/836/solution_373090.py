def busca(a,m):
    x=[]
    for p in m:
        for q in p:
            if q==a:
                list.remove(p,q)
                list.append(x,p)
    return x