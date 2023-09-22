def total(ls,dc):
    l=list(dict.keys(dc))
    m=[]
    k=0
    for i in ls:
        if i in l:
            m.append(dc[i])
    for o in ls:
        k+=o
    return round(o,2)