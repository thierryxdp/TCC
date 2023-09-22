def faltante(N):
    if len[N]==1:
        return 1+(N[0]==1)
    if N[0]====1:
        i=0
        while i<len(N)-1:
            if(N[i+1]-N[1])!=1:
                return N[1]+1
            i+=1
        return len (N)+1
    return 1