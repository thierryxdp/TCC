def filtraMultiplos(x,y):
    v=0
    l=[]
    while v<len(x):
        if x[v]%y==0:
            list.append(l,x[v])
        v=v+1
    return l