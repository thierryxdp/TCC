def maiores(l,n):
    i=0
    a=[]
    for i in range(len(l)):
        if l[i]>n:
            a.append(l[i])
    return a