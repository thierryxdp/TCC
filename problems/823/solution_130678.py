def faltante(L):
    L.append(0)
    i=0
    t=range(1,L[len(L)-1])
    while i<=len(t):
        if L[i]!=t[i]:
            return t[i]
        i+=1