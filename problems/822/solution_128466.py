def repetidos(x):
    n=[]
    c=0
    while c<len(x)-1:
        if x[c]==x[c+1]:
            n.append(1)
        n=n+[1]
    return n