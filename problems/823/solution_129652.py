def faltante(L):
    """coment"""
    l=list(range(1,len(L)+1))
    i = 1
    while i<(len(L)+1):
        if i in l == False:
           return i
        i=i+1