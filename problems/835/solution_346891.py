def melhor_volta(m):
    i=0
    t=[]
    for l in m:
        for a in l:
            t.append(a)
    while min(t) not in m[i]:
        i+=1
    j=i+1
    v=list.index(m[i],min(t))+1
    return (j,min(t),v)