def faltante(L):
    """coment"""
    l=list(range(1,len(L)+1))
    i = 0
    L2=[]
    while i<(len(L)+1):
        if L[i] in l:
            L2=L2+L[i]
            i=i+1
    return L2