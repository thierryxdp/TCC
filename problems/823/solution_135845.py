def faltante(n):
    i=1
    while i<len(n):
        if n[i]!=i:
            return i
        i+=1