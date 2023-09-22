def maiores(l,n):
    a=[]
    list.sort(l)
    i=0
    while n>=l[i]:
        l.remove(l[i])
        i+=1
    return l