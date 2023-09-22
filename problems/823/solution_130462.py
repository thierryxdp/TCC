def faltante(l):
    n=len(l)
    ult=(n+1)
    l2=[1,2,3,4,5,6,7,8]
    i=0
    f=[]
    
    if l[0] != 1:
        return 1
    while i<len(l):
        if l2[i] not in l:
            f = l2[i]
        i=i+1
    return f 
    else:
        return n+1