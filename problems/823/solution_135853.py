def faltante(n):
    i=0
    nn=n.insert(0,0)
    while i<len(n):
        if n[i]!=i:
            return i
        
        i+=1
    return n[-1]+1