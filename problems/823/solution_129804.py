def faltante(L):
    if int.L[0]<int.L[1]:
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