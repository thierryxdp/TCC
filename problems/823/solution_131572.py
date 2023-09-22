def faltante(L):
    if (L[0]!=1):
        return 1
    i=1
    while (i < len(L)):
        if (L[i-1] != L[i]+1):
            x=list.append(L,L[i-1]+1)
        if (L[i-1]==L[i]+1):
            x=list.append(L,L[-1]+1)
        i=i+1
    return list.pop(x,-1)