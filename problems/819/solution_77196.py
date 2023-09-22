def filtraMultiplos(v,n):
    i=0
    v=[]
    while i<len(v):
        if v[i]%n==0:
            list.pop(i)
        else:
            i=i+1
    return v