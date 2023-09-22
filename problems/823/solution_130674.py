def faltante(L):
    i=0
    
    while len(L)>i>0:
        if L[i]-1!=L[i-1]:
            i+=1
    return L[i]+1
print(faltante([3,5]))