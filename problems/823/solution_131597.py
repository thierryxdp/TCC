def faltante(L):
    if (L[0]!=1):
        return 1
    i=1
    x=[]
    list.append(x,L[-1]+1)
    while (i < len(L)):
        if (L[i-1]+1 != L[i]):
            list.clear(x)
            x=[L[i-1]+1]
        i=i+1
    return x[0]