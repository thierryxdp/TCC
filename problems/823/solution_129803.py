def faltante(L):
    if L[0]<L[]:
        i=0
        while i<len(L):
            if L[i] is not i+1:
                return i+1
        	i+=1
    else:
        i=0
        while i<len(L):
            if L[i+1] is not L[i]-1:
                return i+2
            i+=1