def faltante(L):
    i = 0 
    while i+1<len(L):
        if L[i+1] != L[i]+1:
            return L
        i+=1