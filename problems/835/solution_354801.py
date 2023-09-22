def melhor_volta(x):
    L=[]
    for y in x:
       	L.append(min(y))
    o=min(L)
    for z in x:
        if o in z:
            q=x.index(z)+1
            p=z.index(o)+1
    return (q,o,p)