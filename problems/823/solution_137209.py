def faltante(L):
    x=L[0]
    a=0
    for i in L:
        c=i+1
        if c!=x:
            a=i
        x+=1
        
    return a+1