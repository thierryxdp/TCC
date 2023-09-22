def faltante(L):
    c=0
    while c<len(L):
        if L[c] in range(len(L)):
        c+=1
    return L[c]