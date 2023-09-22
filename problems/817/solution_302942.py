def acima_da_media(x):
    if x[0]==x[0]/len(x):
        return[]
    r=0
    for y in x:
        if y>0:
            r=r+y
    med=r/len(x)
    x.append(med)
    x.sort()
    return x[x.index(med)+1:]