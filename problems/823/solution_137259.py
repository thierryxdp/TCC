def faltante(L):
    i=0
    list.sort(L)
    while i<len(L):
        if L[i]+1 not in L: 
            x= L[i]+1
            return x
        if L[i]-1 not in L and i>0:
            x=L[i]-1   
            return x
        i=i+1