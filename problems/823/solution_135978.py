def faltante(L):
    i=0
    difere=[]
    while i<len(L):
        if L[i]!=(i+1):
            difere=difere+[i]
        i=i+1
    del difere[1:]
    return difere