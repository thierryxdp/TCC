def faltante(L):
    x=L[0]
    a=0
    for i in L:
        if i!==x:
            a=i
        x+=1
        
    return a