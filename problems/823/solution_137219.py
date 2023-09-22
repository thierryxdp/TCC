def faltante(L):
    x=1
    a=list(range(L))+[L[len(L)-1]+1]
    for i in a:
        if i not in L:
            return i
        x+=1