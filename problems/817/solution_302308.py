def acima_da_media(l):
     l.sort()
    a=[]
    for i in range(len(l)):
        n=sum(l)/len(l)
        if l[i]>n:
            a.append(l[i])
    return a