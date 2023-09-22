def total(ls,dc):
    l=list(dict.keys(dc))
    m=[]
    k=0
    p=0
    for i in ls:
        if i in l:
            m.append(dc[i])
    while p<=len(m):
        m+=m[k]
        k+=1
    return m