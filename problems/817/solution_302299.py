def maiores(l,n):
    l.sort()
    a=[]
    for i in range(len(l)):
        if l[i]>n:
            a.append(l[i])
    return a