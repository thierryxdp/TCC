def faltante(L):
    if len(L)=L[len(L)-1]:
        return len(L)+1
    for i in L:
        if L[i] != i+1: 
            return i+1