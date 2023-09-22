def filtraMultiplos(ls,n):
    r=[]
    c=0
    while c<len(ls):
        if ls[c]%n==0:
            list.append(r,ls[c])
        c+=1
    return r