def faltante(L):
    x=1
    a=list(range(1,len(L)+2))
    for i in a:
        if i not in L:
            return i
        x+=1