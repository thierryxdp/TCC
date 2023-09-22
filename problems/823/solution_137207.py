def faltante(L):
    x=L[0]
    N=len(L)+2
    a=0
    for i in range(N):
        c=i+1
        if c!=x:
            a=i
        x+=1
        
    return a