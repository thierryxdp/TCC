def filtraMultiplos(l,n):
    l2=[]
    for i in l:
        if i % n == 0:
            l2.append(i)
    return l2