def maiores(l,n):
    list.sort(l)
    a=[]
    i=0
    if n<l[-1]:
        while l[i]<n:
            l.remove(l[i])
            i+=1
        return l
    else:
        return a