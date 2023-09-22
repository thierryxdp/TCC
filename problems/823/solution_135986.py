def faltante(L):
    i=0
    difere=[]
    while i<len(L):
        if L[i]!=(i+1):
            difere=difere+[i+1]
        i=i+1
        else:
            difere=difere+[i-1]
        i=i+1
    return difere