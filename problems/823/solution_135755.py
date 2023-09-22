def faltante(L):
    i=0
    num_falt=0
    while i<len(L):
        if L[i]!=(i+1):
            del L[i+1:]
            num_falt=num_falt+i+1
        i=i+1
        else:
            num_falt=num_falt+len(L)+1
    return num_falt