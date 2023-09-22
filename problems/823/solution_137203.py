def faltante(L):
    x=L[0]
    N=len(L)+1
    for i in range(N):
        if i!=x:
            a=i
        x+=1
        
    return a