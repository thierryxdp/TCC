def total(l,d):
    v=0
    for i in range(len(l)):
        v=v+ d[l[i]]
    v2=round(v,2)
    return v2