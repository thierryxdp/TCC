def total(l,d):
    a=list(dict.keys(d))
    b=list(dict.values(d))
    r=[]
    s=[]
    for e in l:
        if e in a:
            r.append(list.index(a,e))
    for i in r:
        s.append(b[i])
    return round(sum(s),2)