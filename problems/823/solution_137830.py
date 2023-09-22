def faltante(l1):
    i=0
    inteiro=0
    while i<len(l1):
        if l1[i]!=i+1:
            return i
        i+=i+1