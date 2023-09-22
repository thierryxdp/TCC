def faltante(L):
    i=0
    n=1
    while i<len(L):
        if n==L[(i)]:
            n+=1
        i+=1
    return n