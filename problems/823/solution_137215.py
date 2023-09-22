def faltante(L):
    x=1
    a=L+[L[len(L)]+1]
    for i in L:
        if i!=x:
            return i
        x+=1