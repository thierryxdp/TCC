def melhor_volta(x):
    L=[]
    for y in x:
       	L.append(min(y))
    o=min(L)
    for z in x:
        if o in z:
            q=x.index(z)
            p=z.index(o)
    return (q,o,p)