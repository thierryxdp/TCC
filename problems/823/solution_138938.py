def faltante(L):
    c=0
    while c<len(L):
        if L[c] in not range(len(L)):
            return L[c]