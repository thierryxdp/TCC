def filtraMultiplos(v,n):
    i=0
    v=[]
    while i<len(v):
        if v[i]%n==0:
            list.append(v,i)
        i=i+1
    return v